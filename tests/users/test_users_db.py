import pytest
from utils.create_db import create_tables


@pytest.fixture(scope="module", autouse=True)
def ensure_tables():
    """Автоматически создаём таблицы перед тестами (на всякий случай)"""
    create_tables()


def test_insert_and_select_user(db_cursor):
    # Вставляем пользователя
    db_cursor.execute("""
        INSERT INTO users (id, name, email, gender, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (999, "Test User", "test@example.com", "male", "active"))

    # Проверяем, что он появился
    db_cursor.execute("SELECT name, email FROM users WHERE id = %s", (999,))
    result = db_cursor.fetchone()

    assert result[0] == "Test User"
    assert result[1] == "test@example.com"

    # Данные откатятся автоматически после теста (rollback в фикстуре)


def test_user_not_found(db_cursor):
    db_cursor.execute("SELECT * FROM users WHERE id = %s", (999999,))
    result = db_cursor.fetchone()
    assert result is None