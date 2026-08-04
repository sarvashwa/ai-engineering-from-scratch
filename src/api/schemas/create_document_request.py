
from pydantic import BaseModel, ConfigDict, Field

class CreateDocumentRequest(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )

    title: str = Field(
        description="Human-readable title for the document."
        )