from pymongo import MongoClient, ReturnDocument
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client.your_database
locks_collection = db.locks

class DistributedLock:
    def __init__(self, lock_id, lock_ttl=timedelta(minutes=5)):
        self.lock_id = lock_id
        self.lock_ttl = lock_ttl

    def acquire(self):
        now = datetime.now()
        expires_at = now + self.lock_ttl

        # Try to create a new lock
        result = locks_collection.find_one_and_update(
            {"lock_id": self.lock_id, "expires_at": {"$lt": now}},
            {"$set": {"lock_id": self.lock_id, "acquired_at": now, "expires_at": expires_at}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )

        # Check if the lock was successfully acquired
        return result and result["acquired_at"] == now

    def release(self):
        locks_collection.delete_one({"lock_id": self.lock_id})

# Example usage
lock = DistributedLock("resource_123")
if lock.acquire():
    print("Lock acquired. Processing the resource.")
    # Process the resource
    lock.release()
else:
    print("Resource is locked by another process.")
