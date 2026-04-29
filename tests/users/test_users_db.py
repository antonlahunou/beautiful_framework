import pytest
from utils.create_db import create_tables


@pytest.fixture(scope="module", autouse=True)
def ensure_tables():
    create_tables()


@pytest.mark.skip("Waiting for database connection")
def test_insert_and_select_user(db_cursor):
    db_cursor.execute("""
        INSERT INTO users (id, name, email, gender, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (999, "Test User", "test@example.com", "male", "active"))

    db_cursor.execute("SELECT name, email FROM users WHERE id = %s", (999,))
    result = db_cursor.fetchone()

    assert result[0] == "Test User"
    assert result[1] == "test@example.com"

@pytest.mark.skip("Waiting for database connection")
def test_user_not_found(db_cursor):
    db_cursor.execute("SELECT * FROM users WHERE id = %s", (999999,))
    result = db_cursor.fetchone()
    assert result is None