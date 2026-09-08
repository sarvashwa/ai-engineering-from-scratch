from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials

from src.api.dependencies.auth import get_current_token

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

@router.get(
    "-auth",
    summary="testing auth token"
)
def test_auth(
    payload: dict = Depends(get_current_token)
):
    return payload