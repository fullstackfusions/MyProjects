import threading
import logging
from mongoengine import connect, Document, StringField, NotUniqueError, DateTimeField
from datetime import datetime, timezone
import time
from common.config.mongo_config import MongoConfig

mongo_config = MongoConfig.from_env()
mongo_config.client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EventLocks(Document):
    hashed_request = StringField(required=True, unique=True)
    timestamp = DateTimeField(default=datetime.now(timezone.utc))

    meta = {
        'indexes': [
            "#hashed_request",  # Index for hashed_request
            {
                'fields': ['time_stamp'],
                'unique': True,
                'expireAfterSeconds': 30
            }  # Index to expire after 1 hour
        ]
    }

def utc_now():
    return datetime.now(timezone.utc)

def acquire_lock(event_id: str) -> bool:
    try:
        EventLocks(
            hashed_request=event_id,
        ).save()
        logger.info(f"Lock acquired for event_id: {event_id}")
        return True
    except NotUniqueError:
        logger.warning(f"Lock already exists for event_id: {event_id}")
        return False
    except:
        logger.exception(f"Failed to acquire lock for event_id: {event_id}")
        return False

def release_lock(event_id: str) -> bool:
    try:
        EventLocks.objects(hashed_request=event_id).delete()
        logger.info(f"Lock released for event_id: {event_id}")
        return True
    except:
        logger.exception(f"Failed to release lock for event_id: {event_id}")
        return False

def worker(event_id: str, idx: int, results: list):
    logger.info(f"Worker {idx} started for event_id: {event_id}")
    results[idx] = acquire_lock(event_id)

if __name__ == "__main__":
    event_id = "event_12345"
    num_threads = 10
    threads = []
    results = [None] * num_threads

    # Start multiple threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(event_id, i, results))
        threads.append(thread)
        thread.start()
        time.sleep(0.1)  # Slight delay to simulate concurrent access

    for thread in threads:
        thread.join()

    logger.info("All threads completed.")
    print("Results:", results)
    # Only one should be True, others should be False


    # whichever is True is the one that acquired the lock
    # and the rest should be False
    # This demonstrates race condition handling
    # and ensures that only one thread can acquire the lock at a time.
    # Cleanup

    release_lock(event_id)
    logger.info(f"Cleanup completed for event_id: {event_id}")
