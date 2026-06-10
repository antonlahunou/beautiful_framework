from schemas.birds_schemas import *


def test_get_birds_default_pagination(bird_client):
    response = bird_client.get_birds()
    assert response.status_code == 200
    data = response.json()
    BirdListAdapter.validate_python(response.json())
    assert isinstance(data, list)
    assert len(data) <= 20

def test_get_birds_with_pagination(bird_client):
    response = bird_client.get_birds(skip=0, limit=2)
    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 2

def test_get_birds_filter_by_species(bird_client):
    response = bird_client.get_birds(species="Parus major")
    assert response.status_code == 200
    data = response.json()
    if data:
        assert all(bird["species"] == "Parus major" for bird in data)

def test_get_birds_filter_by_device_id(bird_client):
    response = bird_client.get_birds(device_id="emulator")
    assert response.status_code == 200
    data = response.json()
    if data:
        assert all(bird["device_id"] == "emulator" for bird in data)

def test_get_birds_combined_filters(bird_client):
    response = bird_client.get_birds(species="Parus", skip=0, limit=5)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5