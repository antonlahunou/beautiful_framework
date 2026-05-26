import pytest
from clients.posts_client import PostsClient
from factories.post_factory import generate_random_post_data

# @pytest.fixture
# def random_user_payload():
#     data = generate_random_post_data()
#     return {
#         "name": data["name"],
#         "email": data["email"],
#         "gender": data["gender"],
#         "status": data["status"]
#     }