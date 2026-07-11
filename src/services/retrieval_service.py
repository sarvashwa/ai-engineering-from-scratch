from src.services.embedding_service import EmbeddingService
from src.storage.vector_store import VectorStore
from src.models.document_chunk import DocumentChunk

class RetrievalService:
    def __init__(
            self,
            embedding_service: EmbeddingService,
            vector_store: VectorStore,
    ):
        self._embedding_service = embedding_service
        self._vector_store = vector_store

    def retrieve(
            self,
            query: str,
            top_k: int = 5
    ) -> list[DocumentChunk]:
        query_embedding = self._embedding_service.embed_text(query)
        return self._vector_store.search_chunks(
            query_embedding=query_embedding,
            top_k=top_k
        )