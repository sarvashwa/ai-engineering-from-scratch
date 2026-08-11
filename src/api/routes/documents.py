from fastapi import status, APIRouter, Depends

from src.api.dependencies import get_document_service
from src.api.schemas.create_document_request import CreateDocumentRequest
from src.api.schemas.update_document_request import UpdateDocumentRequest
from src.api.schemas.document_response import DocumentResponse
from src.services.document_service import DocumentService

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
    document = service.create_document(request.title, request.user_id)

    return DocumentResponse(
        id=document.id,
        title=document.title,
    )

@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
    summary="Get Document",
    description="Retrieve a document by its ID."
)
def get_document(
    document_id: int,
    service: DocumentService = Depends(get_document_service),
):
    document = service.get_document(document_id)

    return DocumentResponse(
        id=document.id,
        title=document.title,
)

@router.put(
    "/{document_id}",
    response_model=DocumentResponse,
    summary="Update Document",
    description="Update a document by its ID."
)
def update_document(
    document_id: int,
    request: UpdateDocumentRequest,
    service: DocumentService = Depends(get_document_service),
):
    document = service.update_document(document_id, request.title)

    return DocumentResponse(
        id=document.id,
        title=document.title,
    )

@router.delete(
    "/{document_id}",
    summary="Delete Document",
    description="Delete a document by its ID.",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_document(
    document_id: int,
    service: DocumentService = Depends(get_document_service),
):
    service.delete_document(document_id)
    return {"message": f"Document with ID {document_id} has been deleted."}