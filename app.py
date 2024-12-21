import streamlit as st
import cohere
from PyPDF2 import PdfReader
import re
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

# Initialize Cohere client
COHERE_API_KEY = "53ze71FRXFL7oTQjsUqzf8ZG8pI9vuBGItN0Ruq2"  # Replace with your API key
cohere_client = cohere.Client(COHERE_API_KEY)

# Helper Functions
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        try:
            text += page.extract_text() or ""  # Fallback for empty pages
        except Exception as e:
            print(f"Error reading page: {e}")
            continue
    return text

def preprocess_text(text):
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces/newlines with single space
    text = re.sub(r"[^A-Za-z0-9.,;!?()'\"$%\-]+", " ", text)  # Retain $, %, and -
    text = text.strip()
    return text

def chunk_text(text, chunk_size=500, overlap=100):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size - overlap)]

def generate_embeddings(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    return embeddings, model

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def query_faiss_index(index, query_embedding, top_k=5):
    query_embedding = np.array(query_embedding, dtype="float32").reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    return distances, indices

def summarize_with_cohere(text):
    response = cohere_client.summarize(
        text=text,
        length="medium",  # Options: "short", "medium", "long"
        format="paragraph",
    )
    return response.summary

def answer_with_cohere(context, question):
    response = cohere_client.generate(
        prompt=f"Context: {context}\n\nQuestion: {question}\n\nAnswer:",
        max_tokens=200,
        temperature=0.7,
        stop_sequences=["\n"],
    )
    return response.generations[0].text.strip()

# Streamlit App
st.title("ChatPDF: Interactive Q&A with Your PDF")

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "show_end_chat" not in st.session_state:
    st.session_state.show_end_chat = False
if "chat_active" not in st.session_state:
    st.session_state.chat_active = True
if "pdf_summary" not in st.session_state:
    st.session_state.pdf_summary = None
if "embeddings" not in st.session_state:
    st.session_state.embeddings = None
if "embedding_model" not in st.session_state:
    st.session_state.embedding_model = None
if "faiss_index" not in st.session_state:
    st.session_state.faiss_index = None
if "chunks" not in st.session_state:
    st.session_state.chunks = None

# File Upload
pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])
if pdf_file and not st.session_state.pdf_summary:
    # Progress bar for tasks
    progress = st.progress(0)  # Initialize progress bar

    # Extract and preprocess text
    progress.progress(25)  # Update progress bar
    raw_text = extract_text_from_pdf(pdf_file)
    pdf_text = preprocess_text(raw_text)

    # Generate Summary with Cohere
    progress.progress(50)  # Update progress bar
    st.session_state.pdf_summary = summarize_with_cohere(pdf_text)

    # Prepare embeddings
    progress.progress(75)  # Update progress bar
    st.session_state.chunks = chunk_text(pdf_text)
    st.session_state.embeddings, st.session_state.embedding_model = generate_embeddings(st.session_state.chunks)
    st.session_state.faiss_index = create_faiss_index(st.session_state.embeddings)

    # Finalize progress
    progress.progress(100)  # Update progress bar
    st.success("Processing completed. You can now ask questions.")

# Display the PDF summary
if st.session_state.pdf_summary:
    st.subheader("PDF Summary")
    st.write(st.session_state.pdf_summary)

# Display Question Input Only After File Upload
if pdf_file:
    # Chat Interface
    user_question = st.text_input("Type your question here:")
    if st.button("Submit Question"):
        if user_question.strip():
            # Retrieve context
            query_embedding = st.session_state.embedding_model.encode([user_question])
            _, indices = query_faiss_index(st.session_state.faiss_index, query_embedding)
            context = " ".join([st.session_state.chunks[i] for i in indices[0][:5]])  # Combine top 5 chunks

            # Validate Context and Generate Answer
            if not context.strip():
                st.error("No relevant context found. Try rephrasing your question.")
            else:
                with st.spinner("Fetching the answer..."):
                    answer = answer_with_cohere(context, user_question)
                if not answer.strip():
                    answer = "I couldn't find an answer. Please try rephrasing your question."
                st.session_state.chat_history.append({"question": user_question, "answer": answer})
                st.session_state.show_end_chat = True

    # Display chat history with alignment
    for entry in st.session_state.chat_history:
        st.markdown(f"<div style='text-align: right;'><strong>Q:</strong> {entry['question']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: left;'><strong>A:</strong> {entry['answer']}</div>", unsafe_allow_html=True)

    # End Chat Button
    if st.session_state.show_end_chat:
        if st.button("End Chat"):
            st.session_state.chat_history = []
            st.session_state.show_end_chat = False
            st.markdown("<h3 style='text-align: center; color: green;'>Thank you! The chat has been ended. 🌟</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Feel free to upload another file to start a new session!</p>", unsafe_allow_html=True)
