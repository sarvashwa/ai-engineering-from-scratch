from fastapi import Request, Depends
from sqlalchemy.orm import Session

from src.application.application import Application
from src.services.rag_service import RAGService
from src.services.document_ingestion_service import DocumentIngestionService
from src.storage.database import SessionLocal

from src.storage.repositories.document_repository import DocumentRepository
from src.storage.repositories.user_repository import UserRepository

from src.services.document_service import DocumentService
from src.services.user_service import UserService

def get_application(request: Request) -> Application:
    return request.app.state.application

def get_rag_service(
        application: Application = Depends(get_application)
        ) -> RAGService:
    return application.rag_service

def get_document_ingestion_service(
        application: Application = Depends(get_application)
        ) -> DocumentIngestionService:
    return application.document_ingestion_service

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def get_document_repository(
        session: Session = Depends(get_session)
    ) -> DocumentRepository:
    return DocumentRepository(session)

def get_document_service(
        document_repository: DocumentRepository = Depends(get_document_repository),
        session: Session = Depends(get_session)
    ) -> DocumentService:
    return DocumentService(document_repository, session)

def get_user_repository(
        session: Session = Depends(get_session)
    ) -> UserRepository:
    return UserRepository(session)

def get_user_service(
        user_repository: UserRepository = Depends(get_user_repository),
        session: Session = Depends(get_session)
    ) -> UserService:
    return UserService(user_repository, session)
