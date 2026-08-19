from src.main import app

from fastapi.testclient import TestClient

from src.storage.models.user import User

client = TestClient(app)

def test_delete_user_failure(session, override_session):
    response = client.post(
        "/users",
        json={"name": "adam"}
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

def test_create_user_failure():
    response = client.post(
        "/users",
        json={}
    )

    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["type"] == "missing"
    assert data["detail"][0]["loc"] == ["body", "name"]

def test_create_user_with_extra_field():
    response = client.post(
        "/users",
        json={
            "name": "joe",
            "extra": "extra"
        }
    )

    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["type"] == "extra_forbidden"
    assert data["detail"][0]["loc"] == ["body", "extra"]