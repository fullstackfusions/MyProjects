
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


def check_duplicate_mongodb(db, email: str) -> bool:
    try:
        collection = db["users"]
        return collection.find_one({"email": email}) is not None
    except Exception as e:
        print(f"Error checking duplicate: {e}")
        return False

def insert_user_if_not_exists_mongo(db, user: User):
    if not check_duplicate_mongodb(db, user.email):
        insert_data(db, user)
    else:
        print("Duplicate entry. User already exists.")
