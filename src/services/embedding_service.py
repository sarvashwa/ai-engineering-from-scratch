from sentence_transformers import SentenceTransformer
from src.config.config import Settings
from src.utils.timer import Timer

class EmbeddingService:
    def __init__(self, settings: Settings):
        self._model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def embed_text(self, text: str) -> list[float]:
        with Timer("Embedding"):
            return self._model.encode(text).tolist()

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        return self._model.encode(texts).tolist()