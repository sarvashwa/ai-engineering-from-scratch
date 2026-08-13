from src.main import app

from fastapi.testclient import TestClient

from src.storage.models.user import User

client = TestClient(app)

def test_delete_user_failure(session):
    response = client.post(
        "/users",
        params={"name": "joe"}
    )

    user_id = response.json()["id"]

    response = client.post(
    "/documents",
    json={
        "title": "My Document",
        "user_id": user_id
    }
    )

    response = client.delete(
        f"/users/{user_id}"
    )

    assert response.status_code == 409

    data = response.json()

    assert data["detail"] == (
        f"User with ID {user_id} "
        "cannot be deleted because documents still belong to this user."
    )