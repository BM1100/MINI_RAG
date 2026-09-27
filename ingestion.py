from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import pickle


PDF_PATH = "document.pdf"
INDEX_PATH = "vector.index"
CHUNKS_PATH = "chunks.pkl"

reader = PdfReader(PDF_PATH)
text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

print("Characters:", len(text)) 

def chunk_text(text, chunk_size=1000, overlap=200):

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

chunks = chunk_text(text)
print("Number of chunks:", len(chunks))
print("Creating embeddings...")

embedding_model = SentenceTransformer( "all-MiniLM-L6-v2")

embeddings = embedding_model.encode(
    chunks,
    convert_to_numpy=True
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
    pickle.dump(chunks, f)


print("\nIngestion completed successfully!")
print("Saved:", INDEX_PATH)
print("Saved:", CHUNKS_PATH)