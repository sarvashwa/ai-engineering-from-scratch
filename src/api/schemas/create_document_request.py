from pydantic import BaseModel, ConfigDict, Field

class CreateDocumentRequest(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )

    title: str = Field(
        description="The title of the document to create."
    )

    user_id: int = Field(
        description="The ID of the user who owns the document."
    )