from faker import Faker

from schemas.users_schemas import *

fake = Faker()

def test_update_user_name_field(users_client, created_user):
    created_user["name"] = fake.first_name()
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 200

    user = response.json()
    assert user["name"] == created_user["name"]
    assert user["email"] == created_user["email"]
    assert user["gender"] == created_user["gender"]
    assert user["status"] == created_user["status"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == created_user["name"]
    assert user_details["email"] == created_user["email"]
    assert user_details["status"] == created_user["status"]
    assert user_details["gender"] == created_user["gender"]

def test_update_user_email_field(users_client, created_user):
    created_user["email"] = fake.email()
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 200

    user = response.json()
    assert user["name"] == created_user["name"]
    assert user["email"] == created_user["email"]
    assert user["gender"] == created_user["gender"]
    assert user["status"] == created_user["status"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == created_user["name"]
    assert user_details["email"] == created_user["email"]
    assert user_details["status"] == created_user["status"]
    assert user_details["gender"] == created_user["gender"]

def test_update_user_status_field(users_client, created_user):
    if created_user["status"] == "active":
        created_user["status"] = "inactive"
    else:
        created_user["status"] = "active"

    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 200

    user = response.json()
    assert user["name"] == created_user["name"]
    assert user["email"] == created_user["email"]
    assert user["gender"] == created_user["gender"]
    assert user["status"] == created_user["status"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == created_user["name"]
    assert user_details["email"] == created_user["email"]
    assert user_details["status"] == created_user["status"]
    assert user_details["gender"] == created_user["gender"]


def test_update_user_gender_field(users_client, created_user):
    if created_user["gender"] == "male":
        created_user["gender"] = "female"
    else:
        created_user["gender"] = "male"

    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 200

    user = response.json()
    assert user["name"] == created_user["name"]
    assert user["email"] == created_user["email"]
    assert user["gender"] == created_user["gender"]
    assert user["status"] == created_user["status"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == created_user["name"]
    assert user_details["email"] == created_user["email"]
    assert user_details["status"] == created_user["status"]
    assert user_details["gender"] == created_user["gender"]

def test_update_user_with_all_fields(users_client, created_user, random_user_payload):
    response = users_client.update_user(created_user["id"], random_user_payload)
    assert response.status_code == 200

    user = response.json()
    assert user["name"] == random_user_payload["name"]
    assert user["email"] == random_user_payload["email"]
    assert user["gender"] == random_user_payload["gender"]
    assert user["status"] == random_user_payload["status"]

    response = users_client.get_user(user["id"])
    assert response.status_code == 200
    user_details = response.json()

    assert user_details["name"] == random_user_payload["name"]
    assert user_details["email"] == random_user_payload["email"]
    assert user_details["status"] == random_user_payload["status"]
    assert user_details["gender"] == random_user_payload["gender"]

def test_update_user_with_empty_name(users_client, created_user):
    created_user["name"] = ""
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_name_as_none(users_client, created_user):
    created_user["name"] = None
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_empty_email(users_client, created_user):
    created_user["email"] = ""
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_email_as_none(users_client, created_user):
    created_user["email"] = None
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_empty_status(users_client, created_user):
    created_user["status"] = ""
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_status_as_none(users_client, created_user):
    created_user["status"] = None
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_empty_gender(users_client, created_user):
    created_user["gender"] = ""
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_gender_as_none(users_client, created_user):
    created_user["gender"] = None
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_gender_as_trans(users_client, created_user):
    created_user["gender"] = "trans"
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_status_as_dead(users_client, created_user):
    created_user["status"] = "dead"
    response = users_client.update_user(created_user["id"], created_user)
    assert response.status_code == 422

def test_update_user_with_existing_email(users_client, created_user, random_user_payload, mark_user_for_deletion):
    response = users_client.create_user(random_user_payload)
    assert response.status_code == 201
    user = response.json()

    mark_user_for_deletion(user["id"])

    user["email"] = created_user["email"]
    response = users_client.update_user(created_user["id"], user)
    assert response.status_code == 422