from clients.base_client import BaseClient
from configurations import BIRDS_URL

class BirdsClient(BaseClient):
    def get_birds(self, skip: int = 0, limit: int = 20, species: str = None, device_id: str = None):
        params = {"skip": skip, "limit": limit}
        if species:
            params["species"] = species
        if device_id:
            params["device_id"] = device_id
        return self.get(f"{BIRDS_URL}", params=params)

    def get_bird(self, bird_id: int):
        return self.get(f'{BIRDS_URL}{bird_id}')

    def create_bird(self, payload: dict):
        return self.post(f'{BIRDS_URL}', json=payload)

    def update_bird(self, bird_id: int, payload: dict):
        return self.put(f'{BIRDS_URL}{bird_id}', json=payload)

    def delete_bird(self, bird_id: int):
        return self.delete(f'{BIRDS_URL}{bird_id}')