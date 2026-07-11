from src.services.retrieval_service import RetrievalService
from src.services.embedding_service import EmbeddingService
from src.services.prompt_builder import PromptBuilder
from src.storage.vector_store import VectorStore

question = "How does MongoDB store patient data?"
embedding_service = EmbeddingService()

vector_store = VectorStore(
    collection_name = "experiment_11"
)

retrieval_service = RetrievalService(
    embedding_service = embedding_service,
    vector_store= vector_store
    )

retrieval_chunks = retrieval_service.retrieve(
    query = question,
    top_k = 5,
)

prompt_builder = PromptBuilder()

prompt = prompt_builder.build_prompt(
    question = question,
    chunks = retrieval_chunks
)

print("=" * 80)
print("GENERATED PROMPT")
print("=" * 80)
print(prompt)
