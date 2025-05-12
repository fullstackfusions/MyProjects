import logging
import hashlib
from datetime import timezone
from typing import Dict, Optional, List, Any
from enum import Enum, unique, auto
from mongoengine import Document, StringField, DateTimeField, connect, EnumField, NotUniqueError
from datetime import datetime
from marshmallow import Schema
from marshmallow_dataclass import dataclass, add_schema
from dataclasses import field
import json


logger = logging.getLogger(__name__)

# Defining Enum
@unique
class ResponseType(Enum):
    TEXT = auto()
    TEMPLATE = auto()
    EMAIL = auto()
    FORM = auto()

@unique
class RequestType(Enum):
    TEXT = auto()
    FORM = auto()


# Defining Attachment Object dataclass
@dataclass
class AttachmentObject:
    bucket_name: str
    object_key: str

# Defining Request dataclasses
@dataclass
class Request:
    request_type: ResponseType = field(default=ResponseType.UNDEFINED, init=False)

@add_schema
@dataclass
class TextRequest(Request):
    text: str
    request_type: RequestType = field(default=RequestType.TEXT, init=False)

@add_schema
@dataclass
class FormRequest(Request):
    inputs: Dict[Any, Any]
    request_type: RequestType = field(default=RequestType.FORM, init=False)

# Defining Response dataclasses
@dataclass
class Response:
    response_type: ResponseType = field(default=ResponseType.UNDEFINED, init=False)

@add_schema
@dataclass
class FormResponse(Response):
    text: str
    form: str
    form_data: Dict[Any, Any]
    response_type: ResponseType = field(default=ResponseType.FORM, init=False)

@add_schema
@dataclass
class TemplateResponse(Response):
    text: str
    template: str
    template_data: Dict[Any, Any]
    response_type: ResponseType = field(default=ResponseType.TEMPLATE, init=False)

@add_schema
@dataclass
class TextResponse(Response):
    text: str
    markdown: bool
    response_type: ResponseType = field(default=ResponseType.TEXT, init=False)

@add_schema
@dataclass
class EmailResponse(Response):
    recipients: List[str]
    cc_recipients: List[str] = field(default_factory=list)
    bcc_recipients: List[str] = field(default_factory=list)
    subject: str
    body: str
    attachments: List[AttachmentObject] = field(default_factory=list)
    response_type: ResponseType = field(default=ResponseType.EMAIL, init=False)


# Defining the mongoengine schema to cache the responses
class Caches(Document):
    hashed_request = StringField(required=True, unique=True)
    response_data = StringField(required=True)  # Stores JSON string
    response_type = EnumField(required=True)
    timestamp = DateTimeField(default=timezone.utc)
    meta = {
        'indexes': [
            '#hashed_request',  # hashed index  there other types in documentation
            {
                'fields': ['hashed_request', 'response_data', 'response_type', 'timestamp'],
                'expireAfterSeconds': 30   # ttl index
            }
        ]
    }

# Defining the mongoengine schema to check duplicates
class Requests(Document):
    hashed_request = StringField(required=True, unique=True)
    timestamp = DateTimeField(default=timezone.utc)
    meta = {
        'indexes': [
            '#hashed_request',  # hashed index  there other types in documentation
            {
                'fields': ['hashed_request', 'timestamp'],
                'expireAfterSeconds': 10   # ttl index
            }
        ]
    }


# Defining the mongoengine schema to lock the duplicate request to avoid chatbot instance trigger
class Locks(Document):
    request_hash = StringField(required=True, unique=True)
    timestamp = DateTimeField(default=timezone.utc)
    meta = {
        'indexes': [
            '#hashed_request',  # hashed index  there other types in documentation
            {
                'fields': ['request_hash', 'timestamp'],
                'expireAfterSeconds': 10   # ttl index
            }
        ]
    }

# mongodb handler for caches, locks, duplicate requests
class MongoDBCacheManager:

    def __init__(self, host: str, port: str, username: str, password: str, db: str) -> None:
        self._connect_to_database(host, port, username, password, db)

    def _connect_to_database(self, host: str, port: str, username: str, password: str, db: str) -> None:
        connect(
            host=host,
            port=port,
            username=username,
            password=username,
            authSource="$external",
            authMechanism="PLAIN",
            db=db
        )
        logger.info("Daatabase connected")

    def _generate_hash(self, request, user_id = None, room_id=None):
        if user_id and room_id:
            request = (room_id, user_id, request)

        return hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()

    def cache_response(self, request: Request, response: Response):
        # Assuming response is a single dataclass instance for simplicity
        # schema = request.Schema()
        serialized_request = schema.dumps(request)
        # hashed_request = self._generate_hash(serialized_request)

        schema = response.Schema()
        serialized_response = schema.dumps(response)

        cache_entry = Caches(request_hash=serialized_request, response_data=serialized_response, response_type=response.response_type).save()

    def get_cached_response(self, request: Request):
        schema = request.Schema()
        serialized_request = schema.dumps(request)
        hashed_request = self._generate_hash(serialized_request)

        cache_entry = Caches.objects(request_hash=hashed_request).first()

        if not cache_entry:
            return None

        responses = []
        # Dynamically load the schema based on the response_type
        for response_cls in [FormResponse, TextResponse, TemplateResponse, EmailResponse]:  # List all your response classes
            if response_cls.response_type == cache_entry.response_type:
                schema = response_cls.Schema()
                for res in cache_entry.response_data:
                    responses.append(schema.loads(cache_entry.response_data))
        return responses

    def is_duplicate_request(self, user_id: str, room_id: str, request: Request) -> bool:
        """
        Check if the given request hash for a user is a duplicate.
        Returns True if it's a duplicate, False otherwise.
        """
        try:
            schema = request.Schema()
            serialized_request = schema.dumps(request)
            hashed_request = self._generate_hash(serialized_request, user_id=user_id, room_id=room_id)
            Requests(request_hash=hashed_request).save()
            return False  # Not a duplicate if save succeeds
        except NotUniqueError:
            return True  # Duplicate request
