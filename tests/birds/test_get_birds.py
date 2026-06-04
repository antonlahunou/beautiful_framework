from schemas.birds_schemas import *

def test_get_birds(bird_client):
    response = bird_client.get_birds()
    assert response.status_code == 200
    users = BirdListAdapter.validate_python(response.json())
    assert len(users) > 0