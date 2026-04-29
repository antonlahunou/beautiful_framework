from schemas.users_schemas import *

def test_create_user_with_all_fields(users_client, random_user_payload, mark_user_for_deletion):
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user_id = response.json()["id"]

    mark_user_for_deletion(user_id)

def test_create_user_only_with_name_field(users_client):
    response = users_client.create_user({"name": "test_user"})
    assert response.status_code == 422

def test_create_user_with_name_as_empty_string(users_client, random_user_payload):
    random_user_payload["name"] = ""
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_name_as_none(users_client, random_user_payload):
    random_user_payload["name"] = None
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_gender_as_trans(users_client, random_user_payload):
    random_user_payload["gender"] = "trans"
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_status_as_dead(users_client, random_user_payload):
    random_user_payload["status"] = "dead"
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_existing_email(users_client, random_user_payload, mark_user_for_deletion):
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user_id = response.json()["id"]

    mark_user_for_deletion(user_id)

    random_user_payload["name"] = "new"
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422