from fastapi import APIRouter, Depends

from src.api.dependencies.auth import (
    get_current_token,
    get_current_user
)
from src.storage.models import User

router = APIRouter(
    prefix="",
    tags=["test"]
)

@router.get(
    "/test-auth",
    summary="testing auth token"
)
def test_auth(
    payload: dict = Depends(get_current_token)
):
    return payload

@router.get(
    "/current-user",
    summary="testing of current user based on jwt"
)
def current_user(
    user: User = Depends(get_current_user)
):
    return {
        "id": user.id,
        "name": user.name
    }