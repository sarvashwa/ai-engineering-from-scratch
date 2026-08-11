from sqlalchemy.orm import Session

from src.storage.repositories.user_repository import UserRepository

class UserService:
    def __init__(
            self,
            user_repository: UserRepository,
            session: Session
            ):
        
        self._user_repository = user_repository
        self._session = session

    def create_user(self, name: str):
        
        user = self._user_repository.create_user(name)

        return user

    def delete_user(self, user_id: int):
        user = self._user_repository.get_by_id(user_id)

        if user is None:
            raise Exception(f"User with ID {user_id} not found.")

        self._user_repository.delete(user)