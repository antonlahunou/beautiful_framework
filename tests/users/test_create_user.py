from schemas.users_schemas import *

def test_create_user_with_status_as_active(users_client, random_user_payload, mark_user_for_deletion):
    if random_user_payload["status"] == "inactive":
        random_user_payload["status"] = "active"

    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user = response.json()

    mark_user_for_deletion(user["id"])

    assert user["name"] == random_user_payload["name"]
    assert user["email"] == random_user_payload["email"]
    assert user["status"] == random_user_payload["status"]
    assert user["gender"] == random_user_payload["gender"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == random_user_payload["name"]
    assert user_details["email"] == random_user_payload["email"]
    assert user_details["status"] == random_user_payload["status"]
    assert user_details["gender"] == random_user_payload["gender"]

def test_create_user_with_status_as_inactive(users_client, random_user_payload, mark_user_for_deletion):
    if random_user_payload["status"] == "active":
        random_user_payload["status"] = "inactive"

    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user = response.json()

    mark_user_for_deletion(user["id"])

    assert user["name"] == random_user_payload["name"]
    assert user["email"] == random_user_payload["email"]
    assert user["status"] == random_user_payload["status"]
    assert user["gender"] == random_user_payload["gender"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == random_user_payload["name"]
    assert user_details["email"] == random_user_payload["email"]
    assert user_details["status"] == random_user_payload["status"]
    assert user_details["gender"] == random_user_payload["gender"]

def test_create_user_with_gender_as_male(users_client, random_user_payload, mark_user_for_deletion):
    if random_user_payload["gender"] == "female":
        random_user_payload["gender"] = "male"

    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user = response.json()

    mark_user_for_deletion(user["id"])

    assert user["name"] == random_user_payload["name"]
    assert user["email"] == random_user_payload["email"]
    assert user["status"] == random_user_payload["status"]
    assert user["gender"] == random_user_payload["gender"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == random_user_payload["name"]
    assert user_details["email"] == random_user_payload["email"]
    assert user_details["status"] == random_user_payload["status"]
    assert user_details["gender"] == random_user_payload["gender"]

def test_create_user_with_gender_as_female(users_client, random_user_payload, mark_user_for_deletion):
    if random_user_payload["gender"] == "male":
        random_user_payload["gender"] = "female"

    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user = response.json()

    mark_user_for_deletion(user["id"])

    assert user["name"] == random_user_payload["name"]
    assert user["email"] == random_user_payload["email"]
    assert user["status"] == random_user_payload["status"]
    assert user["gender"] == random_user_payload["gender"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == random_user_payload["name"]
    assert user_details["email"] == random_user_payload["email"]
    assert user_details["status"] == random_user_payload["status"]
    assert user_details["gender"] == random_user_payload["gender"]

def test_create_user_only_with_name_field(users_client):
    response = users_client.create_user({"name": "test_user"})
    assert response.status_code == 422

def test_create_user_only_with_email_field(users_client):
    response = users_client.create_user({"email": "test@gmail.com"})
    assert response.status_code == 422

def test_create_user_with_name_as_empty_string(users_client, random_user_payload):
    random_user_payload["name"] = ""
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_name_as_none(users_client, random_user_payload):
    random_user_payload["name"] = None
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_email_as_empty_string(users_client, random_user_payload):
    random_user_payload["email"] = ""
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_email_as_none(users_client, random_user_payload):
    random_user_payload["email"] = None
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_gender_as_empty_string(users_client, random_user_payload):
    random_user_payload["gender"] = ""
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_gender_as_none(users_client, random_user_payload):
    random_user_payload["gender"] = None
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_status_as_empty_string(users_client, random_user_payload):
    random_user_payload["status"] = ""
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 422

def test_create_user_with_status_as_none(users_client, random_user_payload):
    random_user_payload["status"] = None
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