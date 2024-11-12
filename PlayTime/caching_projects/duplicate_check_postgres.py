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

def check_duplicate_postgres(conn, email: str) -> bool:
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM users WHERE email = %s", (email,))
            return cur.fetchone() is not None
    except Exception as e:
        print(f"Error checking duplicate: {e}")
        return False

def insert_user_if_not_exists(conn, user: User):
    if not check_duplicate_postgres(conn, user.email):
        insert_data(conn, user)
    else:
        print("Duplicate entry. User already exists.")
