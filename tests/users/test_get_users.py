import pytest

from schemas.users_schemas import User, UserListAdapter

def test_get_users(users_client):
    response = users_client.get_users()

    assert response.status_code == 200

    users = UserListAdapter.validate_python(response.json())
    assert len(users) > 0

@pytest.mark.skip("Issue n88")
def test_get_user_details(users_client, created_user):
    response = users_client.get_user(created_user["id"])

    assert response.status_code == 200

    user = User.model_validate(response.json())

    assert user.id == created_user["id"]
    assert user.name == created_user["name"]
    assert user.email == created_user["email"]
    assert user.gender == created_user["gender"]
    assert user.status == created_user["status"]