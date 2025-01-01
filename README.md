# PDF-Based RAG Chatbot

This repository hosts a project implementing a **Retrieval-Augmented Generation (RAG)** chatbot that allows querying information from uploaded PDF documents. Built with **Streamlit**, **Cohere API**, **Hugging Face Transformers**, and vector storage, it provides a seamless and efficient way to interact with PDF data.

[Demonstration Video](https://private-user-images.githubusercontent.com/116452492/399582921-9bdbf98c-0339-4a0c-9597-824e42ae2a05.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzU3NTg4ODMsIm5iZiI6MTczNTc1ODU4MywicGF0aCI6Ii8xMTY0NTI0OTIvMzk5NTgyOTIxLTliZGJmOThjLTAzMzktNGEwYy05NTk3LTgyNGU0MmFlMmEwNS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTAxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwMVQxOTA5NDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zNGYzNjRlMTM4OTI4N2RiMGI1MDIyODljMGExOGZhZGE1ZjdhNzRlYWMwMmYwM2RiMjQwODllOTAwZGY1ZDE4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.gu66o7rXPqy2s_EYbNigEXl0VGOzen0DAqqmcX-QpMo)

---

## Features

- **PDF Upload**: Users can upload PDFs, which are processed and indexed for interaction.
- **Concise Summarization**: The uploaded document is summarized using Cohere's API for quick insights.
- **Q&A Interaction**: A chatbot answers user queries based on the PDF's content.
- **User-Friendly Interface**: Streamlit ensures a clean and intuitive UI.
- **Chat History Display**: Previous questions and answers are displayed for context.
- **End Chat Functionality**: Ends the session with a creative "thank you" message.
- **Real-Time Progress Bar**: Visual indicator for processing tasks (e.g., extraction, summarization).

---

## Tech Stack

- **Streamlit**: Web app framework for interactivity.
- **Cohere API**: For text summarization and question-answering.
- **Hugging Face Transformers**: Powered by `google/flan-t5-xxl` for QA.
- **FAISS**: Efficient vector storage and search.
- **PyPDF2**: Text extraction from PDFs.
- **SentenceTransformers**: Text embedding generation.

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
- Cohere API key

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/rag-pdf
   cd rag-pdf
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
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
   - The app generates and displays a concise summary.
3. **Ask Questions**:
   - Interact with the chatbot by entering queries in the text box.
4. **End Chat**:
   - Click "End Chat" to reset the session and display a closing message.

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
- **A**: Directing involves activating efforts to achieve organizational goals through leadership and motivation.

---

## Acknowledgments

- [Cohere API](https://cohere.ai)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io)
