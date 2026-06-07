import os


SERVER_URL = os.getenv("BASE_URL", "https://bird-feeder-api-staging.up.railway.app")

USERS_URL = "/users"
POSTS_URL = "/posts"
COMMENTS_URL = "/comments"
BIRDS_URL = "/birds/"