from fastapi import status, APIRouter, Depends, Header, HTTPException

from src.api.dependencies.services import (
    get_document_service,
    get_document_creation_service,
    get_idempotency_key_service
)
from src.api.schemas.create_document_request import CreateDocumentRequest
from src.api.schemas.update_document_request import UpdateDocumentRequest
from src.api.schemas.document_response import DocumentResponse
from src.api.schemas.error_response import ErrorResponse

from src.services.document_service import DocumentService
from src.services.idempotency_service import IdempotencyService
from src.services.document_creation_service import DocumentCreationService

from src.storage.models import User
from src.api.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.post(
    "",
    response_model=DocumentResponse,
    summary="Create Document",
    description="Create a new document.",
    responses={
        409: {
            "model": ErrorResponse,
            "description": "Idempotency key was already used for a different request.",
        }
    }
)
def create_document(
    request: CreateDocumentRequest,
    idempotency_key: str = Header(..., alias="Idempotency-Key"),
    current_user: User = Depends(get_current_user),
    document_creation_service: DocumentCreationService = Depends(get_document_creation_service),
    idempotency_service: IdempotencyService = Depends(get_idempotency_key_service)
):
    existing = idempotency_service.get_idempotency_key(idempotency_key, current_user.id)
    request_hash = idempotency_service.generate_request_hash(request.model_dump())

    if existing is None:
        idempotency_service.create(
            idempotency_key,
            current_user.id,
            request_hash,
        )
    else:
        if existing.request_hash != request_hash:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"message": "Idempotency key was already used for a different request."},
            )

    document = document_creation_service.create_document(
        request.title,
        current_user.id,
        idempotency_key,
        request_hash
    )

    return DocumentResponse(
        id=document.id,
        title=document.title,
    )

@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
    summary="Get Document",
    description="Retrieve a document by its ID.",
    responses={
        403: {
            "model": ErrorResponse,
            "description": "Access denied to the document.",
        }
    }
)
def get_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
):
    
    document = service.get_document(document_id, current_user)

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
    