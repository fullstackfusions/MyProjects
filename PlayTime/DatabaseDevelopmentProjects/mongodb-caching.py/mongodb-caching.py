from dataclasses import asdict
import hashlib
from datetime import datetime, timedelta
from pymongo import MongoClient
from typing import List, Union

from dataclasses import dataclass, field, asdict
from typing import Dict, Any

# class ResponseType:
#     FORM = "form"
#     TEXT = "text"

# @dataclass
# class Response:
#     pass

# @dataclass
# class ResponseForm(Response):
#     text: str
#     template: str
#     template_data: Dict[Any, Any]
#     response_type: ResponseType = field(default=ResponseType.FORM, init=False)

# @dataclass
# class ResponseText(Response):
#     text: str
#     markdown: bool
#     response_type: ResponseType = field(default=ResponseType.TEXT, init=False)

ResponseType = List[Union[ResponseForm, ResponseText]]

class CacheManager:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["cacheDB"]
        self.collection = self.db["queries"]

    def _generate_hash(self, query):
        return hashlib.sha256(json.dumps(asdict(query), sort_keys=True).encode()).hexdigest()

    def cache_response(self, query: Union[FormRequest, TextRequest], response: ResponseType):
        query_hash = self._generate_hash(query)
        serialized_query = asdict(query)
        serialized_response = [asdict(r) for r in response]
        self.collection.insert_one({
            "query_hash": query_hash,
            "query": serialized_query,
            "response": serialized_response,
            "timestamp": datetime.now()
        })

    def get_cached_response(self, query: Union[FormRequest, TextRequest]) -> Union[ResponseType, None]:
        query_hash = self._generate_hash(query)
        result = self.collection.find_one({
            "query_hash": query_hash,
            "timestamp": {"$gt": datetime.now() - timedelta(days=1)}
        })
        if result:
            return [self._convert_to_response_obj(r) for r in result["response"]]
        return None

    def _convert_to_response_obj(self, response_dict):
        if response_dict.get("response_type") == ResponseType.FORM:
            return ResponseForm(**response_dict)
        elif response_dict.get("response_type") == ResponseType.TEXT:
            return ResponseText(**response_dict)
        return None

# Example usage of CacheManager remains the same
cache_manager = CacheManager()

# Example user query
user_query = {"command": "get_info", "params": {"user_id": 123}}

# Example response
response = [
    ResponseForm(text="Please fill this form", template="form_template", template_data={"field1": "value1"}),
    ResponseText(text="Thank you!", markdown=True)
]

# Check if the response is cached
cached_response = cache_manager.get_cached_response(user_query)

if cached_response:
    print("Cached Response:", cached_response)
else:
    cache_manager.cache_response(user_query, response)
    print("New Response:", response)
