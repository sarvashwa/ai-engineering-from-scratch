
from pydantic import BaseModel, ConfigDict, Field

class DocumentResponse(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )
    
    message: str = Field(
        description="A message indicating the result of the document ingestion operation."
    )