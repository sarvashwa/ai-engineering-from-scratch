from src.services.rag_service import RAGService
from src.services.retrieval_service import RetrievalService
from src.services.prompt_builder import PromptBuilder
from src.services.llm_service import LLMService
from src.services.embedding_service import EmbeddingService
from src.storage.vector_store import VectorStore

from src.config.config import load_settings

settings = load_settings()

embedding_service = EmbeddingService(settings)
vector_store = VectorStore(settings)

retrieval_service = RetrievalService(
    embedding_service,
    vector_store
)
prompt_builder = PromptBuilder()
llm_service = LLMService(settings)

rag_service = RAGService(
    retrieval_service,
    prompt_builder,
    llm_service
)

response = rag_service.stream_answer(
    "How does MongoDB store patient data?",
    top_k = settings.DEFAULT_TOP_K,
)

print("=" * 80)
print("RAG RESPONSE")
print("=" * 80)
for token in response:
    print(token, end="", flush=True)