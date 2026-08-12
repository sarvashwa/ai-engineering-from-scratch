from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.storage.models.base import Base
if TYPE_CHECKING:
    from src.storage.models.document import Document

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(nullable=False)

    documents: Mapped[list["Document"]] = relationship(
        back_populates="user",
        passive_deletes="all",
    )