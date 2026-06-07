import pytest
import allure
from requests import Session


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