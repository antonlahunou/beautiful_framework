from schemas.birds_schemas import *
from utils.assertions import assert_validation_error
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
    assert not bird["confidence"]
    assert not bird["photo_url"]
    assert not bird["audio_url"]
    assert not bird["location_lat"]
    assert not bird["location_lon"]

    response = bird_client.get_bird(bird["id"])
    assert response.status_code == 200
    bird_details = response.json()

    assert bird_details["device_id"] == payload["device_id"]
    assert bird_details["detection_type"] == payload["detection_type"]
    assert bird_details["species"] == payload["species"]
    assert not bird_details["confidence"]
    assert not bird_details["photo_url"]
    assert not bird_details["audio_url"]
    assert not bird_details["location_lat"]
    assert not bird_details["location_lon"]

def test_create_bird_with_empty_device_id(bird_client):
    payload = generate_random_bird_data()
    payload["device_id"] = ""

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="device_id",
                            expected_msg="String should have at least 1 character")

def test_create_bird_only_with_required_device_id_field(bird_client):
    payload = generate_random_bird_data()
    payload.pop("detection_type")
    payload.pop("species")
    payload.pop("confidence")
    payload.pop("photo_url")
    payload.pop("audio_url")
    payload.pop("location_lat")
    payload.pop("location_lon")

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="detection_type", expected_msg="Field required")
    assert_validation_error(response, 422, expected_field="species", expected_msg="Field required")
    
def test_create_bird_only_with_optional_fields(bird_client):
    payload = generate_random_bird_data()
    payload.pop("device_id")
    payload.pop("detection_type")
    payload.pop("species")

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="device_id", expected_msg="Field required")
    assert_validation_error(response, 422, expected_field="detection_type", expected_msg="Field required")
    assert_validation_error(response, 422, expected_field="species", expected_msg="Field required")

def test_create_bird_with_invalid_detection_type_as_image(bird_client):
    payload = generate_random_bird_data()
    payload["detection_type"] = "image"

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="detection_type",
                            expected_msg="detection_type must be one of: audio, video")

def test_create_bird_with_invalid_confidence_lower_than_0(bird_client):
    payload = generate_random_bird_data()
    payload["confidence"] = -1.5

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="confidence",
                            expected_msg="Input should be greater than or equal to 0")

def test_create_bird_with_invalid_confidence_greater_than_1(bird_client):
    payload = generate_random_bird_data()
    payload["confidence"] = 1.5

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="confidence",
                            expected_msg="Input should be less than or equal to 1")

def test_create_bird_with_invalid_latitude_lower_than_minus90(bird_client):
    payload = generate_random_bird_data()
    payload["location_lat"] = -91

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="location_lat",
                            expected_msg="Input should be greater than or equal to -90")

def test_create_bird_with_invalid_latitude_greater_than_90(bird_client):
    payload = generate_random_bird_data()
    payload["location_lat"] = 91

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="location_lat",
                            expected_msg="Input should be less than or equal to 90")

def test_create_bird_with_invalid_longitude_lower_than_minus180(bird_client):
    payload = generate_random_bird_data()
    payload["location_lon"] = -181

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="location_lon",
                            expected_msg="Input should be greater than or equal to -180")

def test_create_bird_with_invalid_longitude_greater_than_180(bird_client):
    payload = generate_random_bird_data()
    payload["location_lon"] = 181

    response = bird_client.create_bird(payload)
    assert_validation_error(response, 422, expected_field="location_lon",
                            expected_msg="Input should be less than or equal to 180")