from datetime import timezone
from datetime import datetime
import hashlib
import json

from sqlalchemy import insert

from src.storage.repositories.idempotency_repository import IdempotencyRepository
from src.storage.models.idempotency_key import IdempotencyKey

class IdempotencyService:
    def __init__(
            self,
            idempotency_repository: IdempotencyRepository,
            ):
        
        self._idempotency_repository = idempotency_repository

    def get_idempotency_key(self, key: str, user_id: int) -> IdempotencyKey | None:
        return self._idempotency_repository.get_by_key_and_user(key, user_id)

    def create(
        self,
        key: str,
        user_id: int,
        request_hash: str,
    ) -> IdempotencyKey | None:

        idempotency_key = IdempotencyKey(
            key=key,
            user_id=user_id,
            request_hash=request_hash,
            status="PROCESSING",
            response_body=None,
            created_at=datetime.now(timezone.utc),
        )

        return self._idempotency_repository.create(idempotency_key)

    def generate_request_hash(self, payload: dict) -> str:
        canonical_payload = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
        )

        return hashlib.sha256(
            canonical_payload.encode("utf-8")
        ).hexdigest()

    def mark_completed(
        self,
        idempotency_key: IdempotencyKey,
        response_body: str,
        ) -> None:

        idempotency_key.status = "Completed"
        idempotency_key.response_body = response_body