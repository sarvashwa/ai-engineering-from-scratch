from fastapi.testclient import TestClient

from src.main import app
from src.security.password import hash_password, verify_password
from src.storage.models import User

client = TestClient(app)
def test_password():
    password = "hello123"

    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True

    wrong_password = "wrong"

    assert verify_password(wrong_password, hashed_password) is False

def test_password_supported_user(session, override_session):
    response = client.post(
    "/users",
    json={
        "name": "jarvis",
        "password": "hello123"
        }
    )

    assert response.status_code == 200
    
    user_id = response.json()["id"]

    user = session.get(User, user_id)

    assert verify_password("hello123", user.password_hash) is True

    assert verify_password(
        "wrong-password",
        user.password_hash
    ) is False