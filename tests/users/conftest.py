import pytest
from clients.users_client import UsersClient
from factories.user_factory import generate_random_user_data

@pytest.fixture(scope="session")
def users_client():
    return UsersClient()

@pytest.fixture
def random_user_payload():
    data = generate_random_user_data()
    return {
        "name": data["name"],
        "email": data["email"],
        "gender": data["gender"],
        "status": data["status"]
    }

@pytest.fixture
def created_user(users_client, random_user_payload):
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user = response.json()
    yield user
    users_client.delete_user(user["id"])

@pytest.fixture
def mark_user_for_deletion(users_client):
    users_to_delete = []

    def track_user(user_id):
        users_to_delete.append(user_id)
        return user_id

    yield track_user

    for user_id in users_to_delete:
        users_client.delete_user(user_id)