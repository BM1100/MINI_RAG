# Mini-RAG 

A lightweight **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about documents and receive answers grounded in the retrieved content.

The project demonstrates the core architecture behind modern RAG applications — from **document ingestion and chunking to semantic search and LLM-based answer generation**.

##  Features

*  Upload and process documents
* Split large documents into smaller chunks
*  Generate semantic embeddings for document chunks
*  Perform similarity-based vector search
*  Generate context-aware answers using an LLM
*  Retrieve relevant document sections before generating responses
*  Lightweight architecture suitable for experimentation and learning
*  Modular ingestion and retrieval pipeline

##  RAG Architecture

```text
                DOCUMENT INGESTION
                       │
                       ▼
                ┌─────────────┐
                │   Document  │
                │    Loader   │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │    Text     │
                │   Chunking  │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │  Embedding  │
                │    Model    │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │ Vector Store│
                └─────────────┘
                       ▲
                       │
                 Similarity Search
                       │
                       │
USER QUERY ────────────┘
     │
     ▼
┌─────────────┐
│   Query     │
│  Embedding  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Retrieve  │
│   Relevant  │
│   Chunks    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│     LLM     │
│ Generation  │
└──────┬──────┘
       │
       ▼
   FINAL ANSWER
```

##  How It Works

### 1. Document Ingestion

Documents are loaded and converted into machine-readable text.

### 2. Chunking

Large documents are divided into smaller overlapping chunks.

Chunking helps the retrieval system identify the most relevant sections instead of passing the entire document to the LLM.

### 3. Embedding Generation

Each chunk is converted into a numerical vector using an embedding model.

Semantically similar pieces of text are represented by vectors that are close to each other in the embedding space.

### 4. Vector Storage

The generated embeddings are stored in a vector database/index for efficient similarity search.

### 5. Query Processing

When a user asks a question, the query is converted into an embedding using the same embedding model.

### 6. Retrieval

The system performs similarity search to retrieve the most relevant document chunks.

### 7. Generation

The retrieved context is combined with the user's question and passed to the language model.

The LLM then generates an answer based on the retrieved information.

##  Tech Stack

* **Python**
* **LLM:** Google Gemini
* **Embeddings:** Sentence Transformers
* **Vector Search:** FAISS
* **Document Processing:** PyPDF
* **RAG Pipeline:** Custom Python implementation

##  Project Structure

```text
Mini-Rag/
│
├── ingestion.py        # Document processing and vector creation
├── retrieval.py        # Query processing and similarity search
├── requirements.txt    # Project dependencies
├── README.md
│
└── data/
    └── documents/      # Input documents
```

> The exact file structure may vary depending on the current implementation.

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/BM1100/MINI-Rag.git
cd MINI-Rag
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Never commit API keys or other secrets to the repository.

### 5. Run the Ingestion Pipeline

```bash
python ingestion.py
```

This processes the documents, creates chunks, generates embeddings and builds the vector index.

### 6. Run the Retrieval Pipeline

```bash
python retrieval.py
```

You can then submit questions and retrieve answers based on the indexed documents.

##  Why RAG?

Traditional LLM applications rely primarily on knowledge encoded during model training. This can lead to problems when the required information is:

* private
* domain-specific
* recently updated
* contained in user-provided documents

RAG addresses this by retrieving relevant external context before generating the response.

Instead
