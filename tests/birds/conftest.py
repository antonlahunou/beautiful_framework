import pytest
from clients.birds_client import BirdsClient
from factories.birds_factory import generate_random_bird_data


@pytest.fixture(scope="session")
def bird_client():
    return BirdsClient()

@pytest.fixture
def created_bird(bird_client):
    data = generate_random_bird_data()
    response = bird_client.create_bird(data)
    assert response.status_code == 201
    bird = response.json()
    yield bird
    bird_client.delete_bird(bird["id"])