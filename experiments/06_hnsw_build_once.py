from sentence_transformers import SentenceTransformer
import chromadb
import time

chunks = [
    f"Document number {i}"
    for i in range(5000)
]
# client = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db")
model = SentenceTransformer("all-MiniLM-L6-v2")
collection = client.get_or_create_collection(
    name="test_collection",
)

documents = []
embeddings = []
ids = []
metadatas = []

for index, chunk in enumerate(chunks):
    embedding = model.encode(chunk)
    documents.append(chunk)
    embeddings.append(embedding)
    ids.append(f"chunk_{index}")
    metadatas.append({"source": "test_chunks", "type": "learning", "section": "rag"})

start = time.perf_counter()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids,
    metadatas=metadatas
)
end = time.perf_counter()

print(f"Ingestion Time: {end - start:.4f} seconds")

print("Insertion Complete")

query_embedding = model.encode("Document 2500")

query_start = time.perf_counter()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

query_end = time.perf_counter()

print(f"Query Time: {query_end - query_start:.6f} seconds")