"""

Benefits of Pydantic or any Model:

- Data Validation: You can use Pydantic for robust data validation before interacting with the database.
- Consistency: The same model can be reused across different databases and operations.
- Ease of Use: Pydantic provides a user-friendly interface for data handling, and using it across both SQL (PostgreSQL) and NoSQL (MongoDB) databases ensures consistent validation.

"""


from pymongo import MongoClient
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Pydantic Model for data validation
class User(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(gt=0)  # Age must be a positive integer


# MongoDB connection parameters
HOST = "localhost"
PORT = 27017
DATABASE = "your_database"
COLLECTION = "users"

# Connect to MongoDB
def connect_mongodb():
    try:
        client = MongoClient(f"mongodb://{HOST}:{PORT}/")
        db = client[DATABASE]
        print("Connected to MongoDB")
        return db
    except Exception as e:
        print(f"Error: {e}")

# Insert data into MongoDB using Pydantic model for validation
def insert_data(db, user: User):
    try:
        collection = db[COLLECTION]
        user_dict = user.dict()  # Convert Pydantic model to dictionary
        result = collection.insert_one(user_dict)
        print(f"Inserted user with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Fetch all data from MongoDB
def fetch_data(db):
    try:
        collection = db[COLLECTION]
        users = collection.find()
        for user in users:
            print(user)
    except Exception as e:
        print(f"Error fetching data: {e}")

# Close the MongoDB connection
def close_connection(client):
    if client:
        client.close()
        print("MongoDB connection closed")


if __name__ == "__main__":
    # Connect to MongoDB
    db = connect_mongodb()

    if db:
        # Insert and validate data using Pydantic
        user_data = User(name="Jane Doe", email="janedoe@example.com", age=28)
        insert_data(db, user_data)

        fetch_data(db)
