
import json

from fastapi import Depends

from sqlalchemy.orm import Session

from src.services.document_service import DocumentService
from src.services.idempotency_service import IdempotencyService

from src.exceptions.idempotency_key_reuse_exception import IdempotencyKeyReuseException
from src.exceptions.idempotency_request_processing_exception import IdempotencyRequestProcessingException

class DocumentCreationService:
    
    def __init__(
        self,
        document_service: DocumentService,
        idempotency_service: IdempotencyService,
        session: Session,
    ):
        self._document_service = document_service
        self._idempotency_service = idempotency_service
        self._session = session
    
    def create_document(
        self,
        title: str,
        user_id: int,
        key: str,
        request_hash: str,
    ):
        existing = self._idempotency_service.get_idempotency_key(
            key,
            user_id,
        )

        if existing is not None:
            if existing.request_hash != request_hash:
                raise IdempotencyKeyReuseException(key)

            if existing.status == "COMPLETED":
                return existing.response_body

            if existing.status == "PROCESSING":
                raise IdempotencyRequestProcessingException(key)

        idempotency_record = self._idempotency_service.create(
            key,
            user_id,
            request_hash,
        )

        document = self._document_service.create_document(
            title,
            user_id,
        )

        response = {
            "id": document.id,
            "title": document.title,
        }

        self._idempotency_service.mark_completed(
            idempotency_record,
            json.dumps(response),
        )

        self._session.commit()

        return response