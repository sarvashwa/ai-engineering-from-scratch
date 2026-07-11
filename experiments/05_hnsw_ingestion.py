from sentence_transformers import SentenceTransformer
import chromadb
import time

chunks = [
    f"Document number {i}"
    for i in range(1000)
]

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
