from pydantic import BaseModel, ConfigDict, Field

class ErrorDetail(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )

    code: int = Field(
        title="Error Code",
        description="Error code"
    )

    message: str = Field(
        title="Error Message",
        description="Error message"
    )

class ErrorResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )

    error: ErrorDetail