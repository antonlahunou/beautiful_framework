import pytest
import psycopg2
from utils.create_db import get_connection

@pytest.fixture(scope="session")
def db_connection():
    conn = get_connection()
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    db_connection.rollback()
    cursor.close()