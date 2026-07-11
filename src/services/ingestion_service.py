import uuid

from typing import Any
from src.models.document_chunk import DocumentChunk
from src.services.embedding_service import EmbeddingService
from src.storage.vector_store import VectorStore

class IngestionService:
    def __init__(
            self,
            embedding_service: EmbeddingService,
            vector_store: VectorStore,
    ):
        self._embedding_service = embedding_service
        self._vector_store = vector_store

    def ingest(
            self,
            chunks: list[str],
            metadata: dict[str, Any],
    ):
        if not chunks:
            return
        
        embeddings = self._embedding_service.embed_texts(chunks)

        document_chunks = []
        
        for index, chunk in enumerate(chunks):

            chunk_metadata = metadata.copy()
            chunk_metadata["chunk_index"] = index

            document_chunk = DocumentChunk(
                id = str(uuid.uuid4()),
                text = chunk,
                embedding = embeddings[index],
                metadata = chunk_metadata
            )

            document_chunks.append(document_chunk)
        self._vector_store.add_chunks(document_chunks)