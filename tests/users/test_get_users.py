import pytest

from schemas.users_schemas import *

def test_get_users(users_client):
    response = users_client.get_users()
    assert response.status_code == 200
    users = UserListAdapter.validate_python(response.json())
    assert len(users) > 0

def test_get_user_details(users_client, created_user):
    response = users_client.get_user(created_user["id"])
    assert response.status_code == 200
    user = User.model_validate(response.json())
    assert user.id == created_user["id"]
    assert user.name == created_user["name"]
    assert user.email == created_user["email"]
    assert user.gender == created_user["gender"]
    assert user.status == created_user["status"]

def test_get_all_users_contain_new_user_details(users_client, created_user):
    response = users_client.get_users()
    assert response.status_code == 200
    users = UserListAdapter.validate_python(response.json())
    new_user = User.model_validate(created_user)
    assert new_user in users

def test_get_not_existing_user_details(users_client):
    response = users_client.get_user(user_id="not_existing_user_id")
    assert response.status_code == 404

def test_get_user_details_after_user_was_deleted(users_client, created_user):
    response = users_client.get_user(user_id=created_user["id"])
    assert response.status_code == 200
    response = users_client.delete_user(user_id=created_user["id"])
    assert response.status_code == 204
    response = users_client.get_user(user_id=created_user["id"])
    assert response.status_code == 404