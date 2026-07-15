from fastapi import APIRouter, Depends

from src.services.document_ingestion_service import DocumentIngestionService
from src.api.schemas.document_request import DocumentRequest
from src.api.schemas.document_response import DocumentResponse
from src.api.dependencies import get_document_ingestion_service

router = APIRouter(
    prefix = "/documents",
    tags = ["Documents"]
)

@router.post(
    "",
    response_model = DocumentResponse,
    summary = "Add Document",
    description = (
    "Ingest a document into the knowledge base for semantic retrieval."
    )
)
def create_document(
    request: DocumentRequest,
    document_ingestion_service: DocumentIngestionService = Depends(get_document_ingestion_service)
):
    document_ingestion_service.ingest_document(
        title = request.title,
        content = request.content
    )

    return DocumentResponse(
        message = "Document ingested successfully."
    )
