from opentelemetry import trace

from src.services.retrieval_service import RetrievalService
from src.services.prompt_builder import PromptBuilder
from src.services.llm_service import LLMService
from src.observability.metrics.metrics import Metrics

tracer = trace.get_tracer(__name__)

class RAGService:
    def __init__(
            self,
            retrieval_service: RetrievalService,
            prompt_builder: PromptBuilder,
            llm_service: LLMService,
            metrics: Metrics
    ):
        self._retrieval_service = retrieval_service
        self._prompt_builder = prompt_builder
        self._llm_service = llm_service
        self._metrics = metrics

    def answer(
            self,
            question: str,
            top_k: int = 5
    ) -> str:
        self._metrics.request_counter.add(1)
        with tracer.start_as_current_span("RAG Service"):
            try:
                chunks = self._retrieval_service.retrieve(question, top_k)
                prompt = self._prompt_builder.build_prompt(question, chunks)
                response = self._llm_service.generate_response(prompt)
                self._metrics.success_counter.add(1)
                return response
            except Exception:
                self._metrics.failed_counter.add(1)
                raise


    def stream_answer(
            self,
            question: str,
            top_k: int = 5
    ):
        with tracer.start_as_current_span("RAG Service"):
            chunks = self._retrieval_service.retrieve(question, top_k)
            prompt = self._prompt_builder.build_prompt(question, chunks)
            response = self._llm_service.generate_response_stream(prompt)
            for token in response:
                yield token