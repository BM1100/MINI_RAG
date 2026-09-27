# Mini-RAG — Multi-Document Retrieval-Augmented Generation System

Mini-RAG is a lightweight Retrieval-Augmented Generation (RAG) system for answering questions from a collection of PDF documents. It combines semantic search with Gemini to generate context-grounded answers from the most relevant sections of the knowledge base.

## Features

* Multi-PDF knowledge base
* Automatically processes all PDFs inside the `knowledge/` folder
* Page-level document metadata
* Text chunking with overlapping windows
* Sentence Transformer embeddings
* FAISS vector similarity search
* Gemini-powered answer generation
* Context-grounded responses
* Interactive multi-turn query loop
* Supports multiple questions in a single session
* `stop` / `end` commands to terminate the session

## Architecture

```text
PDF Documents
     |
     v
Document Extraction
     |
     v
Text Chunking
     |
     v
Sentence Transformer
     |
     v
FAISS Vector Index
     |
     v
User Query
     |
     v
Query Embedding
     |
     v
Similarity Search
     |
     v
Relevant Context
     |
     v
Gemini
     |
     v
Grounded Answer
```

## Project Structure

```text
MINI_Rag/
│
├── knowledge/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── document3.pdf
│
├── ingestion.py
├── retrieval.py
├── vector.index
├── chunks.pkl
├── .env
├── .gitignore
└── requirements.txt
```

## How It Works

### 1. Document Ingestion

`ingestion.py` scans the `knowledge/` directory and processes every PDF found there.

For each document:

1. Extract text using PyPDF.
2. Split the text into overlapping chunks.
3. Store metadata including:

   * PDF filename
   * Page number
   * Chunk text
4. Generate embeddings using `all-MiniLM-L6-v2`.
5. Store the embeddings in a FAISS index.

The resulting vector database is saved as:

```text
vector.index
chunks.pkl
```

### 2. Retrieval

When a user enters a question:

1. The question is converted into an embedding.
2. FAISS searches for the most similar document chunks.
3. The top relevant chunks are retrieved.
4. The retrieved context is passed to Gemini.
5. Gemini generates an answer using the retrieved information.

### 3. Interactive Querying

The system remains active after answering a question, allowing users to ask multiple questions without restarting the application.

```text
Ask a question: What is reinforcement learning?

Answer:
...

Ask a question: What is supervised learning?

Answer:
...

Ask a question: stop
Conversation ended.
```

## Tech Stack

* **Python**
* **PyPDF** — PDF text extraction
* **Sentence Transformers** — semantic embeddings
* **FAISS** — vector similarity search
* **Google Gemini** — context-grounded generation
* **python-dotenv** — environment variable management

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/BM1100/Mini-RAG.git
cd Mini-RAG
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

### 5. Add documents

Place the PDFs you want to query inside:

```text
knowledge/
```

### 6. Build the knowledge base

```bash
python ingestion.py
```

This creates:

```text
vector.index
chunks.pkl
```

### 7. Start the RAG system

```bash
python retrieval.py
```

You can then ask multiple questions during the same session.

Type:

```text
stop
```

or

```text
end
```

to terminate the conversation.

## Current Limitations

* Retrieval currently uses dense vector similarity only.
* Answers depend on the quality of extracted PDF text.
* Scanned/image-only PDFs require OCR.
* The current FAISS index is designed for a local knowledge base.
* Retrieval currently uses a fixed top-K value.

## Future Improvements

* Hybrid search using BM25 + dense retrieval
* Reranking retrieved documents
* Source and page citations in generated answers
* Retrieval evaluation using Recall@K and MRR
* Incremental document ingestion
* Persistent vector databases such as Qdrant or pgvector
* Improved conversational context handling
* Scaling to large document collections
* Retrieval and generation latency optimization
