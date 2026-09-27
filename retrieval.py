import os
import pickle
import faiss

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from google import genai


INDEX_PATH = "vector.index"
CHUNKS_PATH = "chunks.pkl"
load_dotenv()

index = faiss.read_index(INDEX_PATH)

with open(CHUNKS_PATH, "rb") as f:
    chunks = pickle.load(f)
print("Loaded vectors:", index.ntotal)
print("Loaded chunks:", len(chunks))

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

query = input("\nAsk a question: ")

query_embedding = embedding_model.encode(
    [query],
    convert_to_numpy=True
)

k = 3
distances, indices = index.search(
    query_embedding,
    k
)


retrieved_chunks = []

for idx in indices[0]:
    retrieved_chunks.append(chunks[idx])

context = "\n\n".join(
    retrieved_chunks
)

prompt = f"""
You are a document question-answering assistant.
Answer the user's question using ONLY the provided context.
If the answer cannot be found in the context, say:
"I couldn't find the answer in the provided document."

Context:
{context}

Question:
{query}

Answer:
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)


print("\n========== ANSWER ==========")
print(response.text)