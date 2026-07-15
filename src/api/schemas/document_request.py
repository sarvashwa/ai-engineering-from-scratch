from pydantic import BaseModel, ConfigDict, Field

class DocumentRequest(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )

    title: str = Field(
    description="Human-readable title for the document."
)

    content: str = Field(
        description="Document content to be ingested."
    )