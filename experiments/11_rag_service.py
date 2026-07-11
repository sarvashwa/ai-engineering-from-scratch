from src.services.rag_service import RAGService
from src.services.retrieval_service import RetrievalService
from src.services.prompt_builder import PromptBuilder
from src.services.llm_service import LLMService
from src.services.embedding_service import EmbeddingService
from src.storage.vector_store import VectorStore

from src.config.config import Settings

embedding_service = EmbeddingService()
vector_store = VectorStore(Settings.COLLECTION_NAME)

retrieval_service = RetrievalService(
    embedding_service,
    vector_store
)
prompt_builder = PromptBuilder()
llm_service = LLMService()

rag_service = RAGService(
    retrieval_service,
    prompt_builder,
    llm_service
)

answer = rag_service.answer(
    "How does MongoDB store patient data?",
    top_k = Settings.DEFAULT_TOP_K,
)

print("=" * 80)
print("RAG RESPONSE")
print("=" * 80)
print(answer)