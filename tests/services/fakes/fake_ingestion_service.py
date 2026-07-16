from typing import Any

class FakeIngestionService():
    
    def __init__(self):
        self.was_called: bool = False
        self.received_chunks: list[str] | None = None
        self.received_metadata: dict[str, Any] | None = None 

    def ingest(
            self,
            chunks: list[str],
            metadata: dict[str, Any],
    ) -> None:
        
        self.was_called = True
        
        self.received_chunks = chunks.copy()

        self.received_metadata = metadata.copy()