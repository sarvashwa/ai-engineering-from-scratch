from src.services.retrieval_service import RetrievalService
from src.services.prompt_builder import PromptBuilder
from src.services.llm_service import LLMService

class RAGService:
    def __init__(
            self,
            retrieval_service: RetrievalService,
            prompt_builder: PromptBuilder,
            llm_service: LLMService,
    ):
        self._retrieval_service = retrieval_service
        self._prompt_builder = prompt_builder
        self._llm_service = llm_service

    def answer(
            self,
            question: str,
            top_k: int = 5
    ) -> str:
        chunks = self._retrieval_service.retrieve(question, top_k)
        prompt = self._prompt_builder.build_prompt(question, chunks)
        response = self._llm_service.generate_response(prompt)
        return response