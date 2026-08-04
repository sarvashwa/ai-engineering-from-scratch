from sqlalchemy.orm import Session

from src.storage.models.document import Document

class DocumentRepository:

    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, document_id: int) -> Document | None:
        return self._session.get(Document, document_id)
    
    def create(self, document: Document) -> None:
        self._session.add(document)

    def delete(self, document: Document) -> None:
        self._session.delete(document)