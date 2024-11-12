"""
This is mongodb connections and operations class 

you can use AsyncIOMotorClient or MongoClient, both are having same operations

I have used the enum values but the same values should be fetched from config class or environment values for production use cases.

"""

from enum import Enum

class MongoDBEnum(Enum):
    """ MongoDB connection parameters """
    HOST = "localhost"
    PORT = 27017
    DATABASE = "todo_db"
    USER_COLLECTION = "users_collection"
    TODO_COLLECTION = "todo_collection"

    def __call__(self):
        return self.value

# pip install pymongo or pip install motor

import logging
import json
from typing import Dict, Any, AsyncGenerator
# from pymongo import MongoClient  
from motor.motor_asyncio import AsyncIOMotorClient
# from enums import MongoDBEnum
from datetime import datetime, timezone
from bson import ObjectId, json_util

logger = logging.getLogger(__name__)


class MongoDBHandler:
    def __init__(self):
        
        # Connect to MongoDB using AsyncIOMotorClient
        try:
            self.client = AsyncIOMotorClient(f'mongodb://{MongoDBEnum.HOST()}:{MongoDBEnum.PORT()}/')
            self.db = self.client[MongoDBEnum.DATABASE()]
            logger.info("Connected to MongoDB")
        except Exception as e:
            logger.exception("Error connecting to MongoDB: ", e)
        
        # Connect to MongoDB using MongoClient
        # try:
        #     self.client = MongoClient(f'mongodb://{MongoDBEnum.HOST()}:{MongoDBEnum.PORT()}/')
        #     self.db = self.client[MongoDBEnum.DATABASE()]
        #     logger.info("Connected to MongoDB")
        # except Exception as e:
        #     logger.exception("Error connecting to MongoDB: ", e)



    # -----------------------------
    # User Data Operations
    # -----------------------------
    
    async def insert_user_data(self, item: Dict[Any, Any]):
        """ Insert user data into MongoDB """
        try:
            collection = self.db[MongoDBEnum.USER_COLLECTION()]
            result = await collection.insert_one(item)
            logger.info(f"Inserted user with ID: {result.inserted_id}")
        except Exception as e:
            logger.exception("Error inserting user data:", e)

    async def get_user_data(self, username: str) -> dict:
        """ get single user data from MongoDB """
        try:
            collection = self.db[MongoDBEnum.USER_COLLECTION()]
            user = await collection.find_one({"username": username})
            return user
        except Exception as e:
            logger.exception("Error fetching user data:", e)



    # -----------------------------
    # TODO Data Operations
    # -----------------------------
    
    async def insert_todo_data(self, item: Dict[Any, Any]) -> None:
        """ Insert todo data into MongoDB """
        try:
            collection = self.db[MongoDBEnum.TODO_COLLECTION()]
            
            # Explicitly ensure that `created_at` and `updated_at` are Python datetime objects
            item['created_at'] = item.get('created_at', datetime.now(timezone.utc))
            item['updated_at'] = item.get('updated_at', datetime.now(timezone.utc))
            
            return await collection.insert_one(item)
        except Exception as e:
            logger.exception("Error inserting todo data:", e)

    async def get_all_todo_data(self, created_by: str) -> AsyncGenerator[dict, dict]:
        """ Get all todo data for a specific user from MongoDB """
        try:
            print(created_by)
            collection = self.db[MongoDBEnum.TODO_COLLECTION()]
            # Filter to retrieve only the todos for the current user
            async for todo in collection.find({"created_by": created_by}):
                del todo['_id']
                # yield json.loads(json_util.dumps(todo))
                yield todo
        except:
            logger.exception("Error fetching todo data")

    async def get_single_todo_data(self, id: str, created_by: str) -> dict:
        """ Get a single todo data by ID and user from MongoDB """
        try:
            collection = self.db[MongoDBEnum.TODO_COLLECTION()]
            # Filter to retrieve only the todo with the correct id and created_by
            todo = await collection.find_one({"id": id, "created_by": created_by})
            del todo['_id']
            # return json.loads(json_util.dumps(todo))
            return todo
        except:
            logger.exception("Error fetching single todo data")

    async def update_todo_data(self, id: str, updated_data: Dict[Any, Any], created_by: str) -> None:
        """ Update todo data in MongoDB, ensuring the correct user is updating """
        try:
            collection = self.db[MongoDBEnum.TODO_COLLECTION()]
            # Update filter includes both the todo ID and created_by (user's username)
            return await collection.update_one(
                {"id": id, "created_by": created_by},  # Ensure only the owner can update
                {"$set": updated_data}  # Update data and timestamp
            )
        except:
            logger.exception("Error updating todo data")

    async def delete_todo_data(self, id: str, created_by: str) -> None:
        """ Delete todo data from MongoDB """
        try:
            collection = self.db[MongoDBEnum.TODO_COLLECTION()]
            return await collection.delete_one({"id": id, "created_by": created_by})
        except:
            logger.exception("Error deleting todo data")


    # -----------------------------
    # Close the MongoDB connection
    # -----------------------------
    
    def close_connection(self):
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")
