from schemas.birds_schemas import *

def test_get_bird_details(bird_client, created_bird):
    response = bird_client.get_bird(created_bird["id"])
    assert response.status_code == 200
    bird = Bird.model_validate(response.json())
    assert bird.id == created_bird["id"]
    assert bird.device_id == created_bird["device_id"]
    assert bird.detection_type == created_bird["detection_type"]
    assert bird.species == created_bird["species"]
    assert bird.confidence == created_bird["confidence"]
    assert bird.photo_url == created_bird["photo_url"]
    assert bird.audio_url == created_bird["audio_url"]
    assert bird.location_lat == created_bird["location_lat"]
    assert bird.location_lon == created_bird["location_lon"]

def test_get_bird_details_with_not_integer_id(bird_client):
    response = bird_client.get_bird("not_existing_bird_id")
    assert response.status_code == 422

def test_get_not_existing_bird_details(bird_client):
    response = bird_client.get_bird(1488)
    assert response.status_code == 404

def test_get_bird_details_after_bird_was_deleted(bird_client, created_bird):
    response = bird_client.get_bird(created_bird["id"])
    assert response.status_code == 200
    response = bird_client.delete_bird(created_bird["id"])
    assert response.status_code == 204
    response = bird_client.get_bird(created_bird["id"])
    assert response.status_code == 404