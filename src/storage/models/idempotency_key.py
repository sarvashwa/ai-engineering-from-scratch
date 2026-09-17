from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.storage.models import Base

class IdempotencyKey(Base):
    """
    Model for storing idempotency keys in the database.
    """

    __tablename__ = "idempotency_keys"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    key: Mapped[str] = mapped_column(String(255), nullable=False)

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False
    )

    request_hash: Mapped[str] = mapped_column(String(64), nullable=False)

    status: Mapped[str] = mapped_column(String(20), nullable=False)

    response_body: Mapped[str | None] = mapped_column(
        Text, 
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint("key", "user_id"),
    )