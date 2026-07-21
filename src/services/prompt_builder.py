from src.models.document_chunk import DocumentChunk
from src.utils.timer import Timer

class PromptBuilder:
    _PROMPT_TEMPLATE = """You are a helpful AI assistant.

    Use ONLY the provided context to answer the user's question.

    If the answer cannot be found in the context, say:
    "I don't have enough information to answer that."

    Context:

    {context}

    Question:
    {question}

    Answer:
    """

    def __init__(self):
        pass
        
    def build_prompt(
            self,
            question: str,
            chunks: list[DocumentChunk]
            ) -> str:
        context = "\n\n".join(
            chunk.text
            for chunk in chunks
        )
        
        with Timer("Prompt Construction"):
            return self._PROMPT_TEMPLATE.format(
                context=context,
                question=question
            )