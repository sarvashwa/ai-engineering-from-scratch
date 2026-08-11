from sqlalchemy.orm import Session

from src.storage.repositories.document_repository import DocumentRepository
from src.storage.models.document import Document
from src.exceptions.document_not_found_exceptions import DocumentNotFoundException
from src.storage.models.user import User
from src.exceptions.user_not_found_exception import UserNotFoundException
class DocumentService:
    def __init__(
            self,
            document_repository: DocumentRepository,
            session: Session
            ):

        self._document_repository = document_repository
        self._session = session
    
    def create_document(self, title: str, user_id: int) -> Document:
        user = self._session.get(User, user_id)

        if user is None:
            raise UserNotFoundException(user_id)

        document = Document(
            title = title,
            user = user
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

        if document is None:
            raise DocumentNotFoundException(document_id)
    
        return document
    
    def update_document(self, document_id: int, title: str) -> Document:
        document = self._document_repository.get_by_id(document_id)

        if document is None:
            raise DocumentNotFoundException(document_id)
        
        document.title = title

        self._session.commit()

        return document