import pytest
import allure
import psycopg2
from utils.create_db import get_connection
from requests import Session
from clients.users_client import UsersClient
from factories.user_factory import generate_random_user_data

@pytest.fixture(scope="session")
def db_connection():
    conn = get_connection()
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    db_connection.rollback()
    cursor.close()

@pytest.fixture(scope="function", autouse=True)
def attach_request_response():
    original_request = Session.request

    def logged_request(self, method, url, **kwargs):
        request_details = f"{method.upper()} {url}\n\n"
        if "headers" in kwargs:
            request_details += f"Headers:\n{kwargs['headers']}\n\n"
        if "json" in kwargs:
            request_details += f"Body (JSON):\n{kwargs['json']}\n\n"
        elif "data" in kwargs:
            request_details += f"Body (data):\n{kwargs['data']}\n\n"

        allure.attach(
            request_details,
            name=f"Request: {method.upper()} {url}",
            attachment_type=allure.attachment_type.TEXT
        )

        response = original_request(self, method, url, **kwargs)

        response_details = f"Status: {response.status_code}\n\n"
        response_details += f"Headers:\n{dict(response.headers)}\n\n"

        body = response.text[:2000]
        if len(response.text) > 2000:
            body += "\n... (truncated)"
        response_details += f"Body:\n{body}"

        allure.attach(
            response_details,
            name=f"Response: {response.status_code}",
            attachment_type=allure.attachment_type.TEXT
        )
        return response

    Session.request = logged_request
    yield
    Session.request = original_request

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