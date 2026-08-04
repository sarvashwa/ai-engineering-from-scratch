from pydantic import BaseModel, ConfigDict, Field

class CreateDocumentRequest(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )

    id: int = Field(
        description="The ID of the document to update."
    )