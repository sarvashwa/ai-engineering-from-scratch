from pydantic import BaseModel, ConfigDict, Field

class LoginResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )
    
    access_token: str = Field(
        title="Access Token",
        description="Access token to authenticate the user."
    )

    token_type: str = Field(
        title="Token Type",
        description="Type of the token."
    )