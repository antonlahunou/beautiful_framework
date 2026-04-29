from schemas.users_schemas import *

def test_update_user_name_field(users_client, created_user):
    created_user["name"] = "Victor"
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 200