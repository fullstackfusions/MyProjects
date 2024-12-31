"""

Benefits of Pydantic or any Model:

- Data Validation: You can use Pydantic for robust data validation before interacting with the database.
- Consistency: The same model can be reused across different databases and operations.
- Ease of Use: Pydantic provides a user-friendly interface for data handling, and using it across both SQL (PostgreSQL) and NoSQL (MongoDB) databases ensures consistent validation.

"""

import psycopg2
from psycopg2 import sql
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Pydantic Model for data validation
class User(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(gt=0) # Age must be a positive integer


# PostgreSQL connection parameters
HOST = "localhost"
DATABASE = "your_database"
USER = "your_username"
PASSWORD = "your_password"

# Connect to PostgreSQL
def connect_postgres():
    conn = None
    try:
        conn = psycopg2.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD
        )
        print("Connected to PostgreSQL")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        if conn:
            conn.close()

# Create a table
def create_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE NOT NULL,
                age INT
            );
            """)
            conn.commit()
            print("Table 'users' created successfully")
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()

# Insert data into table using Pydantic model for validation
def insert_data(conn, user: User):
    try:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO users (name, email, age) VALUES (%s, %s, %s);
            """, (user.name, user.email, user.age))
            conn.commit()
            print(f"Inserted user {user.name}")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

# Fetch all data from table
def fetch_data(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error fetching data: {e}")

# Close the connection
def close_connection(conn):
    if conn:
        conn.close()
        print("PostgreSQL connection closed")


if __name__ == "__main__":
    # Connect to PostgreSQL
    conn = connect_postgres()
    
    if conn:
        create_table(conn)

        # Insert and validate data using Pydantic
        user_data = User(name="John Doe", email="johndoe@example.com", age=30)
        insert_data(conn, user_data)

        fetch_data(conn)

        close_connection(conn)
