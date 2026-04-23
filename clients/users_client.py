from clients.base_client import BaseClient
from configurations import USERS_URL

class UsersClient(BaseClient):
    def get_users(self):
        return self.get(f'{USERS_URL}')

    def get_user(self, user_id: int):
        return self.get(f'{USERS_URL}/{user_id}')

    def create_user(self, payload: dict):
        return self.post(f'{USERS_URL}', json=payload)

    def update_user(self, user_id: int, payload: dict):
        return self.put(f'{USERS_URL}/{user_id}', json=payload)

    def delete_user(self, user_id: int):
        return self.delete(f'{USERS_URL}/{user_id}')