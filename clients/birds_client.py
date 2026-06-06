from clients.base_client import BaseClient
from configurations import BIRDS_URL

class BirdsClient(BaseClient):
    def get_birds(self):
        return self.get(f'{BIRDS_URL}')

    def get_bird(self, bird_id: int):
        return self.get(f'{BIRDS_URL}{bird_id}')

    def create_bird(self, payload: dict):
        return self.post(f'{BIRDS_URL}', json=payload)

    def update_bird(self, bird_id: int, payload: dict):
        return self.put(f'{BIRDS_URL}{bird_id}', json=payload)

    def delete_bird(self, bird_id: int):
        return self.delete(f'{BIRDS_URL}{bird_id}')