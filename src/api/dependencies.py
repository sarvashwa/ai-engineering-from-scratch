from fastapi import Request, Depends

from src.application.application import Application
from src.services.rag_service import RAGService
from src.services.document_ingestion_service import DocumentIngestionService

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