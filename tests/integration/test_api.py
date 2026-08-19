from src.main import app

from fastapi.testclient import TestClient

from src.storage.models.user import User

client = TestClient(app)

def test_create_user(session, override_session):

    response = client.post(
        "/users",
        json={"name": "jacob"}
    )

    data = response.json()
    user_id = data["id"]

    assert response.status_code == 200
    assert data["name"] == "jacob"
    assert "id" in data

    user = session.get(User, user_id)

    assert user is not None
    assert user.name == "jacob"

def test_delete_user_success(session, override_session):

    response = client.post(
        "/users",
        json={"name": "john"}
    )

    data = response.json()
    user_id = data["id"]

    response = client.delete(
        f"/users/{user_id}"
    )

    assert response.status_code == 200

    user = session.get(User, user_id)

    assert user is None
