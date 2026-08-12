from src.storage.models.user import User

class FakeUserRepository:

    def create_user(self, name):
        return User(
            id=1,
            name=name
        )