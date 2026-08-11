from pydantic import BaseModel, Field, ConfigDict

class CreateUserResponse(BaseModel):
    model_config = ConfigDict(
        extra = "forbid"
    )

    id: int = Field(
        description="The ID of the created user."
    )

    name: str = Field(
        description="The name of the created user."
    )