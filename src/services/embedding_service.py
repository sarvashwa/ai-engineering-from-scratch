from opentelemetry import trace

from sentence_transformers import SentenceTransformer
from src.config.config import Settings
from src.utils.timer import Timer

tracer = trace.get_tracer(__name__)

class EmbeddingService:
    def __init__(self, settings: Settings):
        self._model_name = settings.EMBEDDING_MODEL
        self._model = SentenceTransformer(self._model_name)

    def embed_text(self, text: str) -> list[float]:
        with tracer.start_as_current_span("Embedding Service") as span:
            span.set_attribute("embedding.model", self._model_name)
            span.set_attribute("embedding.text_length", len(text))
            return self._model.encode(text).tolist()

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        return self._model.encode(texts).tolist()