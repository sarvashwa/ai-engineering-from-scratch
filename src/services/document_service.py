from sqlalchemy.orm import Session

from src.storage.repositories.document_repository import DocumentRepository
from src.storage.models.document import Document
from src.exceptions.exceptions import DocumentNotFoundException

class DocumentService:
    def __init__(
            self,
            document_repository: DocumentRepository,
            session: Session
            ):
        self._document_repository = document_repository
        self._session = session
    
    def create_document(self, title: str) -> Document:
        document = Document(
            title = title
        )
        self._document_repository.create(document)
        self._session.commit()
        return document
    
    def delete_document(self, document_id: int) -> None:
        document = self._document_repository.get_by_id(document_id)
        if document is None:
            raise DocumentNotFoundException(document_id)
        self._document_repository.delete(document)
        self._session.commit()
    
    def get_document(self, document_id: int) -> Document:
        document = self._document_repository.get_by_id(document_id)
        return document