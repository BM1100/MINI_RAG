# Mini-RAG

A lightweight **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about documents and receive answers grounded in the retrieved content.

The project demonstrates the core architecture behind modern RAG applications, from **document ingestion and chunking to semantic search and LLM-based answer generation**.

## Features

* Upload and process documents
* Split large documents into smaller chunks
* Generate semantic embeddings for document chunks
* Perform similarity-based vector search
* Generate context-aware answers using an LLM
* Retrieve relevant document sections before generating responses
* Modular ingestion and retrieval pipeline
* Lightweight architecture suitable for experimentation and learning

## RAG Architecture

```text
                DOCUMENT INGESTION
                       |
                       v
                +-------------+
                |  Document   |
                |   Loader    |
                +------+------+ 
                       |
                       v
                +-------------+
                |    Text     |
                |   Chunking  |
                +------+------+
                       |
                       v
                +-------------+
                |  Embedding  |
                |    Model    |
                +------+------+
                       |
                       v
                +-------------+
                | Vector Store|
                +-------------+
                       ^
                       |
                 Similarity Search
                       |
                       |
USER QUERY -----------+
     |
     v
+-------------+
|    Query    |
|  Embedding  |
+------+------+
       |
       v
+-------------+
|   Retrieve  |
|   Relevant  |
|    Chunks   |
+------+------+
       |
       v
+-------------+
|     LLM     |
| Generation  |
+------+------+
       |
       v
   FINAL ANSWER
```

## How It Works

### 1. Document Ingestion

Documents are loaded and converted into machine-readable text.

### 2. Chunking

Large documents are divided into smaller overlapping chunks.

Chunking allows the retrieval system to identify relevant sections instead of passing the entire document to the LLM.

### 3. Embedding Generation

Each chunk is converted into a numerical vector using an embedding model.

Semantically similar pieces of text are represented by vectors that are close to each other in the embedding space.

### 4. Vector Storage

The generated embeddings are stored in a vector index for efficient similarity search.

### 5. Query Processing

When a user asks a question, the query is converted into an embedding using the same embedding model.

### 6. Retrieval

The system performs similarity search to retrieve the most relevant document chunks.

### 7. Generation

The retrieved context is combined with the user's question and passed to the language model.

The LLM generates an answer based on the retrieved information.

## Tech Stack

* Python
* Google Gemini
* Sentence Transformers
* FAISS
* PyPDF
* Custom Python RAG Pipeline

## Project Structure

```text
Mini-Rag/
|
├── ingestion.py        # Document processing and vector creation
├── retrieval.py        # Query processing and similarity search
├── requirements.txt    # Project dependencies
├── README.md
|
└── data/
    └── documents/      # Input documents
```

> The exact file structure may vary depending on the current implementation.

## Getting Started

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

## Why RAG?

Traditional LLM applications rely primarily on knowledge encoded during model training. This can create problems when the required information is:

* Private
* Domain-specific
* Recently updated
* Contained in user-provided documents

RAG addresses this by retrieving relevant external context before generating the response.

Instead of:

```text
Question -> LLM -> Answer
```

the system uses:

```text
Question
   |
   v
Retrieve relevant context
   |
   v
Question + Context
   |
   v
LLM
   |
   v
Grounded Answer
```

## Key Design Decisions

### Chunking

Documents are divided into manageable pieces so retrieval can operate on specific sections rather than entire documents.

### Semantic Retrieval

Embeddings allow the system to retrieve text based on semantic similarity instead of relying only on exact keyword matches.

### Separation of Pipelines

The project separates the ingestion and retrieval processes.

**Ingestion:**

```text
Documents -> Chunks -> Embeddings -> Vector Store
```

**Retrieval:**

```text
Query -> Query Embedding -> Similarity Search -> Context -> LLM
```

This allows document processing to be performed once and reused for multiple queries.

## Limitations

This project is intentionally lightweight and focuses on demonstrating the fundamental RAG pipeline.

Potential limitations include:

* Retrieval quality depends on chunking and embedding quality
* Large document collections require more scalable storage and indexing
* Retrieved context may occasionally be incomplete
* LLMs can still generate incorrect information when retrieved context is insufficient
* No advanced reranking layer is currently implemented

## Future Improvements

* Hybrid search using BM25 and vector search
* Cross-encoder reranking
* Metadata filtering
* Query rewriting
* Multi-query retrieval
* Conversational memory
* Retrieval and generation evaluation
* Scalable vector database
* Distributed document ingestion
* Support for large-scale document collections
* Streaming responses
* Dockerized deployment

## Learning Outcomes

Through this project, I explored:

* Retrieval-Augmented Generation
* Vector embeddings
* Semantic search
* Vector databases
* Document chunking
* LLM prompting
* Information retrieval
* RAG pipeline architecture
* Separation of ingestion and retrieval systems

## Author

**Bhagya Majithiya**

B.Tech — Information and Communication Technology

GitHub: [BM1100](https://github.com/BM1100)
