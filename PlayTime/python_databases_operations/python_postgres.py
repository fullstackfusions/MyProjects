# pip install psycopg2

import psycopg2
from psycopg2 import sql

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

# Insert data into table
def insert_data(conn, name, email, age):
    try:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO users (name, email, age) VALUES (%s, %s, %s);
            """, (name, email, age))
            conn.commit()
            print(f"Inserted user {name}")
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

# Update data in the table
def update_data(conn, user_id, new_age):
    try:
        with conn.cursor() as cur:
            cur.execute("""
            UPDATE users SET age = %s WHERE id = %s;
            """, (new_age, user_id))
            conn.commit()
            print(f"Updated user with ID {user_id}")
    except Exception as e:
        print(f"Error updating data: {e}")
        conn.rollback()

# Delete data from the table
def delete_data(conn, user_id):
    try:
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM users WHERE id = %s;
            """, (user_id,))
            conn.commit()
            print(f"Deleted user with ID {user_id}")
    except Exception as e:
        print(f"Error deleting data: {e}")
        conn.rollback()

# Close the connection
def close_connection(conn):
    if conn:
        conn.close()
        print("PostgreSQL connection closed")


if __name__ == "__main__":
    conn = connect_postgres()
    
    if conn:
        create_table(conn)
        insert_data(conn, "John Doe", "johndoe@example.com", 30)
        fetch_data(conn)
        update_data(conn, 1, 35)  # Update age for user with ID 1
        fetch_data(conn)
        delete_data(conn, 1)  # Delete user with ID 1
        fetch_data(conn)
        close_connection(conn)
