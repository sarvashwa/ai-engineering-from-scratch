from typing import Any

from src.services.ingestion_service import IngestionService

class DocumentIngestionService:
    def __init__(
            self,
            ingestion_service: IngestionService,
            ):
        
        self._ingestion_service = ingestion_service

    def ingest_document(
            self,
            title: str, 
            content: str
        ) -> None:

        chunks = self._chunk_document(
            content = content
            )

        metadata = self._build_metadata(
            title = title
        )
        
        self._ingestion_service.ingest(
            chunks,
            metadata,
            )
    
    def _chunk_document(
        self,
        content: str,
    ) -> list[str]:

        chunks = []

        for paragraph in content.split("\n\n"):

            paragraph = paragraph.strip()

            if paragraph:
                chunks.append(paragraph)

        return chunks

    def _build_metadata(self, title: str) -> dict[str, Any]:
        return {
            "title": title,
        }
