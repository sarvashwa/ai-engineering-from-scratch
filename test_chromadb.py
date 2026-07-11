from sentence_transformers import SentenceTransformer
import chromadb
from test_chunks import chunks

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

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids,
    metadatas=metadatas
)

print(collection)
print(collection.count())
result = collection.get(ids=["chunk_3"])

print(result["documents"][0])