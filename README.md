# PDF-Based RAG Chatbot

This repository contains a project that implements a **Retrieval-Augmented Generation (RAG)** chatbot for querying information from uploaded PDF documents. The project is built using **Streamlit**, **Cohere API**, **Hugging Face Transformers**, and a vector store for efficient information retrieval.

---

## Features

- **Upload PDF**: Users can upload PDF files, which will be processed and indexed for querying.
- **PDF Summarization**: A concise summary of the uploaded PDF is generated using the Cohere API.
- **Question-Answering**: Users can interact with the chatbot by asking questions related to the content of the PDF.
- **Interactive UI**: Clean and user-friendly interface built with Streamlit.
- **Chat History**: Displays previous questions and answers for better context.
- **End Chat**: A feature to reset the session and display a creative "thank you" message.
- **Progress Bar**: Visual indicator for processing steps like extraction, summarization, and embedding generation.

---

## Tech Stack

- **Streamlit**: For building the interactive web app.
- **Cohere API**: For summarizing the PDF content.
- **Hugging Face Transformers**: For QA tasks using `google/flan-t5-xxl`.
- **ChromaDB**: For vector storage and retrieval.
- **PyPDF2**: For extracting text from PDFs.
- **SentenceTransformers**: For generating vector embeddings.

---

## Folder Structure

```
├── app.py                   # Main Streamlit application
├── chunk_text.py            # Handles text chunking
├── extract_pdf.py           # PDF text extraction logic
├── generate_embeddings.py   # Embedding generation functions
├── query.py                 # Handles vector store querying
├── vector.py                # Vector store creation and management
├── requirements.txt         # Python dependencies
├── POM_UNIT_4.pdf           # Example PDF file
```

---

## Setup and Installation

### Prerequisites

- Python 3.9+
- A Cohere API key

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/rag-pdf
   cd rag-pdf
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key**:
   - Add your Cohere API key to a `.env` file in the project root:
     ```
     COHERE_API_KEY=your-cohere-api-key
     ```

5. **Run the App**:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Upload a PDF**:
   - Click the "Upload your PDF" button and select a file.
2. **View Summary**:
   - A summary of the document will be displayed.
3. **Ask Questions**:
   - Type your question in the text box and click "Submit Question."
   - The chatbot will fetch the answer based on the document's content.
4. **End Chat**:
   - Click the "End Chat" button to reset the session and display a closing message.

---

## Example Interaction

### Upload
- **File**: `POM_UNIT_4.pdf`

### Summary
```
Motivation is a key concept in directing and leadership, emphasizing various models like Maslow's Hierarchy of Needs...
```

### Chat
- **Q**: What is the definition of directing?
- **A**: Directing involves activating efforts to achieve organizational goals, often through leadership and motivation.

---

## Acknowledgments

- [Cohere API](https://cohere.ai)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io)
