import chromadb

from opentelemetry import trace

from src.config.config import Settings
from src.models.document_chunk import DocumentChunk
from src.utils.timer import Timer

tracer = trace.get_tracer(__name__)
class VectorStore:
    def __init__(self, settings: Settings):
        self._client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_PATH
        )

        self._collection = self._client.get_or_create_collection(
            name=settings.COLLECTION_NAME
        )

    def add_chunks(self, chunks: list[DocumentChunk]):
        if not chunks:
            return

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:
            ids.append(chunk.id)
            documents.append(chunk.text)
            embeddings.append(chunk.embedding)
            metadatas.append(chunk.metadata)

        self._collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def count_chunks(self) -> int:
        return self._collection.count()
    
    def search_chunks(
            self, 
            query_embedding: list[float],
            top_k: int = 5
        ) -> list[DocumentChunk]:
        
        with tracer.start_as_current_span("Vector Search"):
            results = self._collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
            )
        
            return [
            DocumentChunk(
                id=chunk_id,
                text=document,
                metadata=metadata,
            )
            for chunk_id, document, metadata in zip(
                results["ids"][0] or [],
                results["documents"][0] or [],
                results["metadatas"][0] or [],
            )
            ]
    
    def list_chunks(self) -> list[DocumentChunk]:
        results = self._collection.get()
        return [
        DocumentChunk(
            id=chunk_id,
            text=document,
            metadata=metadata,
        )
        for chunk_id, document, metadata in zip(
            results["ids"] or [],
            results["documents"] or [],
            results["metadatas"] or [],
        )
        ]
    
    def clear_collection(self) -> None:
        results = self._collection.get()

        if results["ids"]:
            self._collection.delete(
                ids=results["ids"]
            )