import pytest
from clients.users_client import UsersClient

@pytest.fixture(scope="session")
def users_client():
    return UsersClient()

@pytest.fixture
def random_user_payload():
    return {
        "name": "Leo",
        "email": "ads@gmail.com",
        "gender": "male",
        "status": "active"
    }

@pytest.fixture
def created_user(users_client, random_user_payload):
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user = response.json()
    yield user
    users_client.delete_user(user["id"])