import psycopg2

from config.settings import POSTGRES_PASSWORD


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        user="test_user",
        password=POSTGRES_PASSWORD,
        database="test_db"
    )

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            gender VARCHAR(10),
            status VARCHAR(10)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("USERS table created")

if __name__ == "__main__":
    create_tables()