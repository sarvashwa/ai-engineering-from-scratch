from fastapi import Depends

from sqlalchemy.orm import Session

from src.storage.repositories.document_repository import DocumentRepository
from src.storage.repositories.user_repository import UserRepository

from src.api.dependencies.database import get_session

def get_document_repository(
        session: Session = Depends(get_session)
    ) -> DocumentRepository:
    return DocumentRepository(session)


def get_user_repository(
        session: Session = Depends(get_session)
    ) -> UserRepository:
    return UserRepository(session)

