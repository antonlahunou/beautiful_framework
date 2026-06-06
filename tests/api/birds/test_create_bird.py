from schemas.birds_schemas import *
from factories.birds_factory import generate_random_bird_data

def test_create_bird_with_detection_type_as_video(bird_client, mark_bird_for_deletion):
    payload = generate_random_bird_data()
    if payload["detection_type"] == "audio":
        payload["detection_type"] = "video"

    response = bird_client.create_bird(payload)
    assert response.status_code == 201
    bird = response.json()

    mark_bird_for_deletion(bird["id"])

    assert bird["device_id"] == payload["device_id"]
    assert bird["detection_type"] == payload["detection_type"]
    assert bird["species"] == payload["species"]
    assert bird["confidence"] == payload["confidence"]
    assert bird["photo_url"] == payload["photo_url"]
    assert bird["audio_url"] == payload["audio_url"]
    assert bird["location_lat"] == payload["location_lat"]
    assert bird["location_lon"] == payload["location_lon"]

    response = bird_client.get_bird(bird["id"])
    assert response.status_code == 200
    bird_details = response.json()

    assert bird_details["device_id"] == payload["device_id"]
    assert bird_details["detection_type"] == payload["detection_type"]
    assert bird_details["species"] == payload["species"]
    assert bird_details["confidence"] == payload["confidence"]
    assert bird_details["photo_url"] == payload["photo_url"]
    assert bird_details["audio_url"] == payload["audio_url"]
    assert bird_details["location_lat"] == payload["location_lat"]
    assert bird_details["location_lon"] == payload["location_lon"]

def test_create_bird_with_detection_type_as_audio(bird_client, mark_bird_for_deletion):
    payload = generate_random_bird_data()
    if payload["detection_type"] == "video":
        payload["detection_type"] = "audio"

    response = bird_client.create_bird(payload)
    assert response.status_code == 201
    bird = response.json()

    mark_bird_for_deletion(bird["id"])

    assert bird["device_id"] == payload["device_id"]
    assert bird["detection_type"] == payload["detection_type"]
    assert bird["species"] == payload["species"]
    assert bird["confidence"] == payload["confidence"]
    assert bird["photo_url"] == payload["photo_url"]
    assert bird["audio_url"] == payload["audio_url"]
    assert bird["location_lat"] == payload["location_lat"]
    assert bird["location_lon"] == payload["location_lon"]

    response = bird_client.get_bird(bird["id"])
    assert response.status_code == 200
    bird_details = response.json()

    assert bird_details["device_id"] == payload["device_id"]
    assert bird_details["detection_type"] == payload["detection_type"]
    assert bird_details["species"] == payload["species"]
    assert bird_details["confidence"] == payload["confidence"]
    assert bird_details["photo_url"] == payload["photo_url"]
    assert bird_details["audio_url"] == payload["audio_url"]
    assert bird_details["location_lat"] == payload["location_lat"]
    assert bird_details["location_lon"] == payload["location_lon"]

def test_create_bird_only_with_required_fields(bird_client, mark_bird_for_deletion):
    payload = generate_random_bird_data()
    payload.pop("confidence")
    payload.pop("photo_url")
    payload.pop("audio_url")
    payload.pop("location_lat")
    payload.pop("location_lon")

    response = bird_client.create_bird(payload)
    assert response.status_code == 201
    bird = response.json()

    mark_bird_for_deletion(bird["id"])

    assert bird["device_id"] == payload["device_id"]
    assert bird["detection_type"] == payload["detection_type"]
    assert bird["species"] == payload["species"]
    assert "confidence" not in bird
    assert "photo_url" not in bird
    assert "audio_url" not in bird
    assert "location_lat" not in bird
    assert "location_lon" not in bird

    response = bird_client.get_bird(bird["id"])
    assert response.status_code == 200
    bird_details = response.json()

    assert bird_details["device_id"] == payload["device_id"]
    assert bird_details["detection_type"] == payload["detection_type"]
    assert bird_details["species"] == payload["species"]
    assert "confidence" not in bird_details
    assert "photo_url" not in bird_details
    assert "audio_url" not in bird_details
    assert "location_lat" not in bird_details
    assert "location_lon" not in bird_details

# def test_create_user_only_with_name_field(users_client):
#     response = users_client.create_user({"name": "test_user"})
#     assert response.status_code == 422
#
#
# def test_create_user_with_status_as_dead(users_client, random_user_payload):
#     random_user_payload["status"] = "dead"
#     response = users_client.create_user(random_user_payload)
#     assert response.status_code == 422