import pytest
from unittest.mock import Mock

from tests.services.fakes.fake_user_repository import FakeUserRepository
from src.services.user_service import UserService


class TestCreateUserServiceUsingMock:
    def test_create_user_service(self):
        
        #Arrange
        repository = FakeUserRepository()
        session = Mock()

        session.commit.side_effect = Exception("Commit failed")

        service = UserService(
            repository,
            session
        )

        #Act
        with pytest.raises(Exception):
            service.create_user("John Doe 1")

        #Assert
        session.commit.assert_called_once()
        session.rollback.assert_called_once()