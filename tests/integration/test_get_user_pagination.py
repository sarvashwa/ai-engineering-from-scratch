from src.main import app

from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_user_pagination(session, override_session):
    names = ["test-1", "test-2", "test-3", "test-4", "test-5"]

    created_users = []

    for name in names:
        response = client.post(
            "/users",
            json={"name": name}
        )

        assert response.status_code == 200

        created_users.append(response.json())

    response = client.get(
        "/users",
        params={"skip": 2, "limit": 2}
    )

    
    data = response.json()

    print (data)

    # assert response.status_code == 200

    # assert [user["name"] for user in response.json()] == [
    #     "test-3",
    #     "test-4"
    # ]

def test_get_users_negative_skip():
    response = client.get(
        "/users",
        params={"skip": -1}
    )

    assert response.status_code == 422

def test_get_users_limit_too_large():
    response = client.get(
        "/users",
        params={"limit": 101}
    )

    assert response.status_code == 422

def test_get_users_empty_page(session, override_session):
    response = client.get(
        "/users",
        params={"skip": 100, "limit": 10}
    )

    assert response.status_code == 200
    assert response.json() == []