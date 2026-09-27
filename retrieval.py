import os
import pickle
import faiss

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load FAISS index
index = faiss.read_index("vector.index")

# Load chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

print("Knowledge base loaded.")
print("Total chunks:", len(chunks))

# Load embedding model
print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

print("\nRAG is ready!")
print("Type 'stop' or 'end' to exit.\n")

while True:

    # User query
    query = input("Ask a question: ").strip()

    # Exit condition
    if query.lower() in ["stop", "end"]:
        print("Conversation ended.")
        break

    if not query:
        continue

    # Convert query into embedding
    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )

    # Search FAISS
    k = 5
    distances, indices = index.search(
        query_embedding,
        k
    )

    # Get relevant chunks
    context = ""

    for idx in indices[0]:
        chunk = chunks[idx]
        context += chunk["text"] + "\n\n"

    # Create prompt
    prompt = f"""
Answer the question using only the context below.

If the answer is not present in the context,
say "I don't know."

Question:
{query}

Context:
{context}
"""

    # Generate answer
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nAnswer:")
    print(response.text)
    print("\n" + "-" * 60 + "\n")