from sqlalchemy.orm import Session

from src.storage.repositories.idempotency_repository import IdempotencyRepository
from src.storage.models.idempotency_key import IdempotencyKey

class IdempotencyService:
    def __init__(
            self,
            idempotency_repository: IdempotencyRepository,
            ):
        
        self._idempotency_repository = idempotency_repository

    def get_idempotency_key(self, key: str, user_id: int) -> IdempotencyKey:
        return self._idempotency_repository.get_by_key_and_user(key, user_id)

    def create(self, idempotency_key: IdempotencyKey):
        self._idempotency_repository.create(idempotency_key)