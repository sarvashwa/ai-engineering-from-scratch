from sqlalchemy.orm import Session
from src.storage.models.idempotency_key import IdempotencyKey

class IdempotencyRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_by_key_and_user(self, key: str, user_id: int) -> IdempotencyKey | None:
        return self._session.query(IdempotencyKey).filter(
            IdempotencyKey.key == key, IdempotencyKey.user_id == user_id
        ).first()

    def create(self, idempotency_key = IdempotencyKey) -> None:

        self._session.add(idempotency_key)
        self._session.flush()

        return idempotency_key
