from dataclasses import dataclass

@dataclass
class DocumentChunk:
    id: str
    text: str
    metadata: dict[str, str]
    embedding: list[float] | None = None