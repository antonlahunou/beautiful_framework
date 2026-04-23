import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("ACCESS_TOKEN not set. Check .env file or environment variables.")