from src.services.embedding_service import EmbeddingService
from src.storage.vector_store import VectorStore
from src.services.ingestion_service import IngestionService

embedding_service = EmbeddingService()

vector_store = VectorStore(
    collection_name="experiment_11"
)

ingestion_service = IngestionService(
    embedding_service,
    vector_store,
)

chunks = [
    "Dependency Injection allows components to receive dependencies rather than creating them.",
    "Middleware wraps the request-response lifecycle to implement cross-cutting concerns.",
    "Exception handlers convert Python exceptions into HTTP responses.",
    "Configuration management separates application settings from business logic.",
]

metadata = {
    "source": "experiment_11"
}

ingestion_service.ingest(
    chunks,
    metadata
)

print(f"Chunks in collection: {vector_store.count_chunks()}")