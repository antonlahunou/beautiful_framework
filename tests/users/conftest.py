import pytest

@pytest.fixture
def mark_user_for_deletion(users_client):
    users_to_delete = []

    def track_user(user_id):
        users_to_delete.append(user_id)
        return user_id

    yield track_user

    for user_id in users_to_delete:
        users_client.delete_user(user_id)