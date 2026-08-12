from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.storage.models.base import Base
if TYPE_CHECKING:
    from src.storage.models.user import User
    from src.storage.models.embedding import Embedding


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    title: Mapped[str] = mapped_column(nullable=False)

    summary: Mapped[str | None] = mapped_column(nullable=True)

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="RESTRICT",
            ),
        nullable=True
    )

    user: Mapped["User"] = relationship(
        back_populates="documents"
    )

    embeddings: Mapped[list["Embedding"]] = relationship(
        back_populates="document",
        cascade="all, delete-orphan"
    )