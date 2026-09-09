import jwt

from fastapi import Request, Depends, status, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.api.dependencies.repositories import get_user_repository
from src.storage.repositories.user_repository import UserRepository
from src.storage.models.user import User
from src.storage.models.document import Document
from src.exceptions.user_not_found_exception import UserNotFoundException

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

def get_current_user(
        payload: dict = Depends(get_current_token),
        user_repository: UserRepository = Depends(get_user_repository),
    ) -> User:

    user_id = int(payload["sub"])

    user = user_repository.get_by_id(user_id)

    if not user:
        raise UserNotFoundException(user_id)

    return user
    
def require_document_owner(
        document: Document,
        current_user: User = Depends(get_current_user)
    ) -> None:
    if document.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this document",
        )
    
    return document