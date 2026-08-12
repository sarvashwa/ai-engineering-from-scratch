import pytest

from tests.services.fakes.fake_session import FakeSession
from tests.services.fakes.fake_user_repository import FakeUserRepository
from src.services.user_service import UserService

class TestCreateUserService:
    def test_create_user_service(self):
        
        #Arrange
        repository = FakeUserRepository()
        session = FakeSession()

        service = UserService(
            repository,
            session
        )

        #Act
        with pytest.raises(Exception):
            service.create_user("John Doe 1")

        #Assert
        assert session.rollback_called == True
        assert session.should_commit_fail == True