
from pydantic import BaseModel, Field, ConfigDict

class CreateUserRequest(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )

    name: str = Field(
        description="Name for the new user."
    )
