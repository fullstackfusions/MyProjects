import psycopg2
from pydantic import BaseModel

# Pydantic Model for validation
class User(BaseModel):
    name: str
    email: str
    age: int


def connect_postgres():
    conn = psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_user",
        password="your_password"
    )
    return conn


def lock_event(conn, user_id: int):
    try:
        with conn.cursor() as cur:
            # Lock the row for update
            cur.execute("SELECT * FROM users WHERE id = %s FOR UPDATE", (user_id,))
            user_data = cur.fetchone()
            if user_data:
                print(f"Locked row: {user_data}")
                # Perform any operation while the row is locked
                cur.execute("UPDATE users SET age = age + 1 WHERE id = %s", (user_id,))
                conn.commit()
                print(f"Updated user with ID: {user_id}")
            else:
                print("User not found")
    except Exception as e:
        print(f"Error during locking: {e}")
        conn.rollback()


if __name__ == "__main__":
    conn = connect_postgres()
    lock_event(conn, 1)  # Example: Lock user with ID 1
    conn.close()
