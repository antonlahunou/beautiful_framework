from clients.base_client import BaseClient
from configurations import POSTS_URL

class PostsClient(BaseClient):
    def get_posts(self, user_id: int):
        return self.get(f'/{user_id}{POSTS_URL}')

    def create_post(self, user_id: int, payload: dict):
        return self.post(f'/{user_id}{POSTS_URL}', json=payload)