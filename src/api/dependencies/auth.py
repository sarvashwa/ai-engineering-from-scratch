import jwt

from fastapi import Request, Depends, status, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.security.token import verify_access_token

security = HTTPBearer()

def get_current_token(
        credentials: HTTPAuthorizationCredentials = Depends(security)
    ) -> dict:
    try:
        return verify_access_token(credentials.credentials)
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )