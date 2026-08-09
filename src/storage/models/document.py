from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.storage.models.base import Base

class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    title: Mapped[str] = mapped_column(nullable=False)

    summary: Mapped[str | None] = mapped_column(nullable=True)

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )