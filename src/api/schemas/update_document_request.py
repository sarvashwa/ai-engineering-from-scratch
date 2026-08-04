from pydantic import BaseModel, ConfigDict, Field

class UpdateDocumentRequest(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )
    
    title: str = Field(
        description="The updated title for the document."
    )