from pathlib import Path
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import pickle


KNOWLEDGE_DIR = Path("Knowledge_Source")
INDEX_PATH = "vector.index"
CHUNKS_PATH = "chunks.pkl"

CHUNK_SIZE = 1000
OVERLAP = 200

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


pdf_files = sorted(KNOWLEDGE_DIR.glob("*.pdf"))

if not pdf_files:
    print("No PDF files found in knowledge folder.")
    exit()


print(f"Found {len(pdf_files)} PDF(s).")
print()


all_chunks = []

for pdf_path in pdf_files:

    print(f"Processing: {pdf_path.name}")

    reader = PdfReader(pdf_path)

    document_chunks = []

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if not page_text:
            continue

        page_chunks = chunk_text(page_text)

        for chunk in page_chunks:

            chunk_data = {
                "text": chunk,
                "source": pdf_path.name,
                "page": page_number
            }

            all_chunks.append(chunk_data)

            document_chunks.append(chunk_data)

    print(f"Pages: {len(reader.pages)}")
    print(f"Chunks: {len(document_chunks)}")
    print()

if not all_chunks:
    print("No text could be extracted from the PDFs.")
    exit()


print("Total chunks:", len(all_chunks))
print("Creating embeddings...")

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

texts = [
    chunk["text"]
    for chunk in all_chunks
]

embeddings = embedding_model.encode(
    texts,
    convert_to_numpy=True,
    show_progress_bar=True
)


print("Embedding shape:", embeddings.shape)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("Vectors stored:", index.ntotal)

faiss.write_index(
    index,
    INDEX_PATH
)

with open(CHUNKS_PATH, "wb") as f:
    pickle.dump(all_chunks, f)
print("\nIngestion completed successfully!")

print("Saved:")
print(f"  - {INDEX_PATH}")
print(f"  - {CHUNKS_PATH}")

print("\nKnowledge Base:")
for pdf in pdf_files:
    print(f"  - {pdf.name}")