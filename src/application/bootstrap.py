from src.application.application import Application

from src.services.embedding_service import EmbeddingService
from src.services.ingestion_service import IngestionService
from src.services.retrieval_service import RetrievalService
from src.services.document_ingestion_service import DocumentIngestionService
from src.services.prompt_builder import PromptBuilder
from src.services.llm_service import LLMService
from src.services.rag_service import RAGService
from src.config.config import Settings

from src.storage.vector_store import VectorStore

def create_application(
    settings: Settings,
) -> Application:
    
    embedding_service = EmbeddingService(settings)
    
    vector_store = VectorStore(settings)

    ingestion_service = IngestionService(
        embedding_service = embedding_service,
        vector_store = vector_store,
    )

    document_ingestion_service = DocumentIngestionService(
        ingestion_service = ingestion_service,
    )

    retrieval_service = RetrievalService(
        embedding_service = embedding_service,
        vector_store = vector_store,
    )

    prompt_builder = PromptBuilder()

    llm_service = LLMService(settings)

    rag_service = RAGService(
        retrieval_service = retrieval_service,
        prompt_builder = prompt_builder,
        llm_service = llm_service,
    )

    return Application(
        embedding_service=embedding_service,
        vector_store=vector_store,
        document_ingestion_service=document_ingestion_service,
        ingestion_service=ingestion_service,
        retrieval_service=retrieval_service,
        prompt_builder=prompt_builder,
        llm_service=llm_service,
        rag_service=rag_service,
    )