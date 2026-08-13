import pytest
from sqlalchemy.exc import IntegrityError

from unittest.mock import Mock

from src.storage.models.user import User
from src.services.user_service import UserService
from src.exceptions.user_has_document_exception import UserHasDocumentException

class TestDeleteUserService:
    def test_delete_user_with_document(self):

        #Arrange
        repository = Mock()
        session = Mock()

        user = User(
            id = 3,
            name = "Sarvashwa"
        )

        repository.get_by_id.return_value = user

        repository.delete.side_effect = IntegrityError(
            "delete failed",
            None,
            None
        )

        service = UserService(
            repository,
            session
        )

       
        #Act
        with pytest.raises(UserHasDocumentException):
            service.delete_user(3)

        #Assert
        repository.get_by_id.assert_called_once_with(3)
        repository.delete.assert_called_once_with(user)
        session.rollback.assert_called_once()
        session.commit.assert_not_called()