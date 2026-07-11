from src.services.retrieval_service import RetrievalService
from src.services.embedding_service import EmbeddingService
from  src.storage.vector_store import VectorStore

embedding_service = EmbeddingService()
vector_store = VectorStore(
    collection_name="learning"
)

retrieval_service = RetrievalService(
    embedding_service=embedding_service,
    vector_store=vector_store
)

retrieved_chunks = retrieval_service.retrieve(
    query="How does MongoDB store patient data?",
    top_k=5
)

print(f"Retrieved {len(retrieved_chunks)} chunks")
print()

for index, chunk in enumerate(retrieved_chunks, start=1):
    print(f"Result {index}")
    print(f"Text: {chunk.text}")
    print(f"Source: {chunk.metadata['source']}")
    print(f"Chunk Index: {chunk.metadata.get('chunk_index')}")
    print("-" * 50)
