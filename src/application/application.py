from dataclasses import dataclass
from src.services.llm_service import LLMService
from src.services.prompt_builder import PromptBuilder
from src.services.rag_service import RAGService
from src.services.retrieval_service import RetrievalService
from src.services.embedding_service import EmbeddingService
from src.services.ingestion_service import IngestionService
from src.storage.vector_store import VectorStore


@dataclass
class Application:
    embedding_service: EmbeddingService
    vector_store: VectorStore
    ingestion_service: IngestionService
    retrieval_service: RetrievalService
    prompt_builder: PromptBuilder
    llm_service: LLMService
    rag_service: RAGService

    def shutdown(self) -> None:
        """
        Release application-owned resources.

        Currently, there are no resources requiring explicit cleanup.
        """
        print("release application")
        pass