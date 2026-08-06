from pydantic import BaseModel, ConfigDict, Field

class CreateDocumentRequest(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )

    title: str = Field(
        description="The title of the document to create."
    )