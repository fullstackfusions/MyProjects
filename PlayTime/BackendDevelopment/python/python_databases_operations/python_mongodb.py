# pip install pymongo

from pymongo import MongoClient

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

# Insert data into MongoDB
def insert_data(db, name, email, age):
    try:
        collection = db[COLLECTION]
        user = {"name": name, "email": email, "age": age}
        result = collection.insert_one(user)
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

# Update data in MongoDB
def update_data(db, email, new_age):
    try:
        collection = db[COLLECTION]
        result = collection.update_one({"email": email}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Updated user with email {email}")
        else:
            print("No user found to update")
    except Exception as e:
        print(f"Error updating data: {e}")

# Delete data from MongoDB
def delete_data(db, email):
    try:
        collection = db[COLLECTION]
        result = collection.delete_one({"email": email})
        if result.deleted_count > 0:
            print(f"Deleted user with email {email}")
        else:
            print("No user found to delete")
    except Exception as e:
        print(f"Error deleting data: {e}")

# Close the MongoDB connection
def close_connection(client):
    if client:
        client.close()
        print("MongoDB connection closed")


if __name__ == "__main__":
    # Connect to MongoDB
    db = connect_mongodb()

    if db:
        # Insert, fetch, update, and delete operations
        insert_data(db, "Jane Doe", "janedoe@example.com", 28)
        fetch_data(db)
        update_data(db, "janedoe@example.com", 35)
        fetch_data(db)
        delete_data(db, "janedoe@example.com")
        fetch_data(db)
