from fastapi import APIRouter, Depends

from api.schemas.document_response import DocumentResponse
from src.services.document_service import DocumentService
from src.api.schemas.create_document_request import CreateDocumentRequest
from src.api.schemas.document_response import DocumentResponse
from src.api.dependencies import get_document_service


router = APIRouter(
    prefix = "/documents",
    tags = ["Documents"]
)

@router.get(
    "/{document_id}",
    response_model = DocumentResponse,
    summary = "Get Document",
    description = (
    "Retrieve a document by its ID."
    )
)
def get_document(
    request: CreateDocumentRequest,
    service: DocumentService = Depends(get_document_service)
):
    document = service.create_document(document_id=request.document_id)
    if document is None:
        return {"message": "Document not found."}
    
    return DocumentResponse(
        id = document.id,
        title = document.title
    )