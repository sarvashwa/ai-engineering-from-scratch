
from pydantic import BaseModel, ConfigDict, Field

class DocumentResponse(BaseModel):
    message: str