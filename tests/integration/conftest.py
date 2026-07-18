import pytest

from src.config.config import load_settings
from src.storage.vector_store import VectorStore
from src.services.embedding_service import EmbeddingService
from src.services.ingestion_service import IngestionService
from src.services.document_ingestion_service import DocumentIngestionService

@pytest.fixture
def settings():
    settings = load_settings()
    settings.COLLECTION_NAME = "test_document"
    return settings

@pytest.fixture
def vector_store(settings):
    vector_store = VectorStore(settings)
    vector_store.clear_collection()
    return vector_store

@pytest.fixture
def embedding_service(settings):
    return EmbeddingService(settings)

@pytest.fixture
def ingestion_service(vector_store, embedding_service):
    return IngestionService(
        vector_store = vector_store,
        embedding_service = embedding_service,
    )


@pytest.fixture
def document_ingestion_service(ingestion_service):
    return DocumentIngestionService(
        ingestion_service = ingestion_service
    )