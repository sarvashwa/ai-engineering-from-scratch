from pydantic import BaseModel, Field, ConfigDict

class LoginRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )
    name: str = Field(
        description="Name of the user to login."
    )

    password: str = Field(
        description="Password of the user to login."
    )