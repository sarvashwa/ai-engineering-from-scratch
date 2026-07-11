import time
from sentence_transformers import SentenceTransformer
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

model = SentenceTransformer("all-MiniLM-L6-v2")

collection = client.get_collection(
    name="test_collection"
)

question = "What database was used?"

question_embedding = model.encode(question)

start = time.time()

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=5
)

end = time.time()

for i, (doc, dist) in enumerate(zip(results['documents'][0], results['distances'][0])):
    print(f"Result {i + 1}\n")
    print(f"Document:\n{doc}\n")
    print(f"Distance:\n{dist:.4f}\n\n")

print(f"ChromaDB retrieval time: {end - start:.4f} seconds")