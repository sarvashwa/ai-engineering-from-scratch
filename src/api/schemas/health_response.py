from pydantic import BaseModel, StrictStr, ConfigDict

class HealthResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )
    status: str
    version: StrictStr
    active: bool
