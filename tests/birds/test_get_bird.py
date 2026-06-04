from schemas.birds_schemas import *

def test_get_user_details(bird_client, created_bird):
    response = bird_client.get_bird(created_bird["id"])
    assert response.status_code == 200
    bird = Bird.model_validate(response.json())