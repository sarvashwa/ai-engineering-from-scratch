from sqlalchemy import insert
from sqlalchemy.orm import Session

from src.storage.models.idempotency_key import IdempotencyKey

class IdempotencyRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_by_key_and_user(self, key: str, user_id: int) -> IdempotencyKey | None:
        return self._session.query(IdempotencyKey).filter(
            IdempotencyKey.key == key, IdempotencyKey.user_id == user_id
        ).first()

    def create(
        self,
        idempotency_key: IdempotencyKey,
    ) -> IdempotencyKey | None:

        statement = (
            insert(IdempotencyKey)
            .values(
                key=idempotency_key.key,
                user_id=idempotency_key.user_id,
                request_hash=idempotency_key.request_hash,
                status=idempotency_key.status,
                response_body=idempotency_key.response_body,
                created_at=idempotency_key.created_at,
            )
            .on_conflict_do_nothing(
                index_elements=["key", "user_id"]
            )
            .returning(IdempotencyKey)
        )

        result = self._session.execute(statement)

        return result.scalar_one_or_none()
