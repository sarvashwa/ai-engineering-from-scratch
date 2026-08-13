import pytest

from unittest.mock import Mock

from src.exceptions.user_not_found_exception import UserNotFoundException
from src.services.user_service import UserService

class TestGetUserNotFound:

    def test_get_user_not_found(self):

        #Arrange
        repository = Mock()
        session = Mock()

        repository.get_by_id.return_value = None

        service = UserService(
            repository,
            session
        )

        #Act
        with pytest.raises(UserNotFoundException):
            service.get_user(999)

        #Assert
        repository.get_by_id.assert_called_once_with(999)
        session.commit.assert_not_called()
        session.rollback.assert_not_called()
        
