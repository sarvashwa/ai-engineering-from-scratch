from tests.services.fakes.fake_ingestion_service import FakeIngestionService
from src.services.document_ingestion_service import DocumentIngestionService

def test_called_ingestion_service():
     #Arrange
    fake = FakeIngestionService()

    document_ingestion_service = DocumentIngestionService(
        ingestion_service = fake,
    )

    #Act
    document_ingestion_service.ingest_document(
        title = "FastAPI",
        content = "Paragraph 1\n\nParagraph 2"
    )

    #Assert
    assert fake.was_called

def test_passes_correct_chunks():
     #Arrange
    fake = FakeIngestionService()

    document_ingestion_service = DocumentIngestionService(
        ingestion_service = fake,
    )

    #Act
    document_ingestion_service.ingest_document(
        title = "FastAPI",
        content = "Paragraph 1\n\nParagraph 2"
    )

    #Assert
    assert fake.received_chunks == ["Paragraph 1", "Paragraph 2"]

def test_passes_correct_metadata():
     #Arrange
    fake = FakeIngestionService()

    document_ingestion_service = DocumentIngestionService(
        ingestion_service = fake,
    )

    #Act
    document_ingestion_service.ingest_document(
        title = "FastAPI",
        content = "Paragraph 1\n\nParagraph 2"
    )

    #Assert
    assert fake.received_metadata == {"title": "FastAPI"}