import requests

from configurations import *
from scr.pydantic_schemas.pydantic_user_schemas import User, UserListAdapter

def test_get_users(say_hello):
    response = requests.get(f'{SERVER_URL}{GET_USERS}')

    assert response.status_code == 200

    users = UserListAdapter.validate_python(response.json())
    assert len(users) > 0

def test_another():
    assert True