from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.storage.repositories.user_repository import UserRepository
from src.exceptions.user_has_document_exception import UserHasDocumentException
from src.exceptions.user_not_found_exception import UserNotFoundException

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
            raise UserNotFoundException(user_id)

        try:
            self._user_repository.delete(user)
        except IntegrityError:
            self._session.rollback()
            raise UserHasDocumentException(user_id)