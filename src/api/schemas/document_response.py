from pydantic import BaseModel, ConfigDict, Field

class DocumentResponse(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )
    id: int = Field(
        description="The ID of the created document."
    )
    title: str = Field(
        description="The title of the created document."
    )   