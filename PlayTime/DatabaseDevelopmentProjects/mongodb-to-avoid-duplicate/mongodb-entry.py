"""
This class covers caching the requests and responses in mongodb
This class covers duplicate requests check and sends proper response for duplicates
This class covers distributed lock for multi instance block
"""


from pymongo import MongoClient, errors
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from typing import Dict, Any, Union
import hashlib
import json

# Assuming ResponseForm, ResponseText, FormRequest, TextRequest, ResponseType are defined

class CacheManager:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["cacheDB"]
        self.queries_collection = self.db["queries"]
        self.requests_collection = self.db["requests"]
        self.locks_collection = self.db["locks"]

        # Set up unique indexes on 'hash' field
        self._setup_unique_hash_index(self.queries_collection)
        self._setup_unique_hash_index(self.requests_collection)
        self._setup_unique_hash_index(self.locks_collection)

        # Set up TTL indexes
        self._setup_ttl_index(self.locks_collection, "expires_at", 300)      # 5 minutes for locks
        self._setup_ttl_index(self.queries_collection, "timestamp", 86400)   # 24 hours for cached responses
        self._setup_ttl_index(self.requests_collection, "timestamp", 300)    # 5 minutes for duplicate checks

    def _setup_unique_hash_index(self, collection):
        index_name = "hash_unique"
        if index_name not in collection.index_information():
            collection.create_index("hashed_request", unique=True, name=index_name)

    def _setup_ttl_index(self, collection, field_name, ttl_seconds):
        index_name = f"{field_name}_ttl"
        if index_name not in collection.index_information():
            collection.create_index([(field_name, 1)], expireAfterSeconds=ttl_seconds, name=index_name)

    def acquire_lock(self, event_id):
        try:
            self.locks_collection.insert_one({
                "hashed_request": event_id,
                "expires_at": datetime.utcnow() + timedelta(minutes=5)
            })
            return True
        except errors.DuplicateKeyError:
            return False

    def release_lock(self, event_id):
        self.locks_collection.delete_one({"hashed_request": event_id})

    def _generate_hash(self, request, user_id = None):

        if user_id:
            request_dict = {user_id: self._dataclass_to_dict(request)}
        else:
            request_dict = self._dataclass_to_dict(request)
        return hashlib.sha256(json.dumps(request_dict), sort_keys=True).encode().hexdigest()

    def _dataclass_to_dict(obj):
        if is_dataclass(obj):
            # Convert dataclass to dict
            obj_dict = asdict(obj)
            # Process each field
            for key, value in obj_dict.items():
                if isinstance(value, Enum):
                    # Convert Enum to its value (or name) for serialization
                    obj_dict[key] = value.name
            return obj_dict
        return obj

    def cache_response(self, request: Union[FormRequest, TextRequest], response: ResponseType):
        hashed_request = self._generate_hash(request)
        serialized_request = self._dataclass_to_dict(request)
        serialized_response = [self._dataclass_to_dict(r) for r in response]
        self.queries_collection.insert_one({
            "hashed_request": hashed_request,
            "request": serialized_request,
            "response": serialized_response,
            "timestamp": datetime.utcnow()
        })

    def get_cached_response(self, request: Union[FormRequest, TextRequest]) -> Union[ResponseType, None]:
        hashed_request = self._generate_hash(request)
        result = self.queries_collection.find_one({
            "hashed_request": hashed_request,
            "timestamp": {"$gt": datetime.utcnow() - timedelta(minutes=300)}
        })
        if result:
            return [self._convert_to_response_obj(r) for r in result["response_payload"]]
        return None

    def _convert_to_response_obj(self, response_dict):
        response_type = response_dict.pop("response_type", None)

        if response_type == ResponseType.FORM.name:
            obj = FormResponse(**response_dict)
            obj.response_type = ResponseType.FORM
            return obj
        elif response_type == ResponseType.TEXT.name:
            obj = TextResponse(**response_dict)
            obj.response_type = ResponseType.TEXT
            return obj

        return None


    def is_duplicate_request(self, user_id, request, cooldown_minutes=5):
        hashed_request = self._generate_hash(request)
        current_time = datetime.utcnow()
        try:
            self.requests_collection.insert_one({
                "hashed_request": hashed_request,
                "user_id": user_id,
                "request": asdict(request),
                "timestamp": current_time
            })
            return False
        except errors.DuplicateKeyError:
            existing_request = self.requests_collection.find_one({"hashed_request": hashed_request})
            if existing_request and (current_time - existing_request["timestamp"]) < timedelta(minutes=cooldown_minutes):
                return True
            else:
                self.requests_collection.update_one(
                    {"hashed_request": hashed_request},
                    {'$set': {"timestamp": current_time}}
                )
                return False

    def delete_request_entry(self, user_id, request):
        hashed_request = self._generate_hash(request)
        self.requests_collection.delete_one({"hashed_request": hashed_request})




# Example usage remains the same
cache_manager = CacheManager()

user_id = 123  # Example user ID
request = FormRequest(inputs={"field": "value"})  # Example query
event_id = "some_unique_event_id"  # Example event ID


# Try to acquire lock
if cache_manager.acquire_lock(event_id):

    # Check for duplicate request
    if not cache_manager.is_duplicate_request(user_id, request):
        # Proceed with the query processing
        cached_response = cache_manager.get_cached_response(request)
        if cached_response:
            print("Cached Response:", cached_response)
        else:
            # Example response
            response = [ResponseForm(text="Form response", template="form_template", template_data={"field1": "value1"})]
            cache_manager.cache_response(request, response)
            print("New Response:", response)
        cache_manager.delete_request_entry(user_id, request)  # Clean up after processing
    else:
        print("Duplicate request is still in progress.")
    cache_manager.release_lock(event_id)
else:
    # Lock is held by another instance
    print("Another instance is processing this event.")

