from fastapi import APIRouter, Depends

from src.api.dependencies import get_document_service
from src.api.schemas.create_document_request import CreateDocumentRequest
from src.api.schemas.document_response import DocumentResponse
from src.services.document_service import DocumentService
from src.exceptions.exceptions import DocumentNotFoundException

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.post(
    "",
    response_model=DocumentResponse,
    summary="Create Document",
    description="Create a new document."
)
def create_document(
    request: CreateDocumentRequest,
    service: DocumentService = Depends(get_document_service),
):
    document = service.create_document(request.title)

    return DocumentResponse(
        id=document.id,
        title=document.title,
    )

@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
    summary="Find Document",
    description="Find a document by its ID."
)
def get_document(
    document_id: int,
    service: DocumentService = Depends(get_document_service),
):
    document = service.get_document(document_id)

    if document is None:
        raise DocumentNotFoundException(document_id)

    return DocumentResponse(
        id=document.id,
        title=document.title,
)