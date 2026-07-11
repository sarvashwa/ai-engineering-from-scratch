from pydantic import BaseModel, Field, ConfigDict

class AskRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )
    question: str = Field(
        min_length=5,
        max_length=500,
        description="The question to ask the RAG system.",
        examples=["What is Retrieval-Augmented Generation?"],
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=10,
        description="Number of documents to retrieve before generating an answer.",
        examples=[3],
    )