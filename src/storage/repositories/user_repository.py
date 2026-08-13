
from sqlalchemy.orm import Session
from typing import Optional

from src.storage.models.user import User

class UserRepository:
    def __init__(self, session: Session):
        self._session = session

    def create_user(self, name: str) -> User:
        user = User(
            name=name
        )
        
        self._session.add(user)

        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        try:
            return self._session.get(User, user_id)
        except Exception:
            raise

    def delete(self, user: User) -> None:
    
        try:
            self._session.delete(user)
        except Exception:
            raise