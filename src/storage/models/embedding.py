from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.storage.models.base import Base

if TYPE_CHECKING:
    from src.storage.models.document import Document


class Embedding(Base):
    __tablename__ = "embeddings"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    document_id: Mapped[int] = mapped_column(
        ForeignKey(
            "documents.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    document: Mapped["Document"] = relationship(
        back_populates="embeddings"
    )