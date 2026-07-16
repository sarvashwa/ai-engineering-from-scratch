from src.storage.vector_store import VectorStore
from src.services.embedding_service import EmbeddingService
from src.services.ingestion_service import IngestionService
from src.services.document_ingestion_service import DocumentIngestionService
from src.config.config import load_settings

def test_document_integration():

    #Arrange
    settings = load_settings()
    settings.COLLECTION_NAME = "test_documents"

    vector_store = VectorStore(settings)
    
    embedding_service = EmbeddingService(settings)

    ingestion_service = IngestionService(
        embedding_service = embedding_service,
        vector_store = vector_store,
    )

    document_ingestion_service = DocumentIngestionService(
        ingestion_service = ingestion_service
    )

    #Act

    vector_store.clear_collection()
    
    document_ingestion_service.ingest_document(
        title = "FastAPI",
        content = "Paragraph 1\n\nParagraph 2",
    )


    #Assert
    chunks = vector_store.list_chunks()

    assert len(chunks) == 2

    expected_texts = {
        "Paragraph 1",
        "Paragraph 2",
    }

    actual_texts = {
        chunk.text
        for chunk in chunks
    }

    assert actual_texts == expected_texts

    expected_chunk_index = {0, 1}

    actual_chunk_index = {
        chunk.metadata["chunk_index"]
        for chunk in chunks
    }

    assert actual_chunk_index == expected_chunk_index

    assert all(
        chunk.metadata["title"] == "FastAPI"
        for chunk in chunks
    )