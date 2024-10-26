import os
from dataclasses import field
from marshmallow_dataclass import dataclass
from object_storage import ObjectStorage

@dataclass
class StorageConfig:
    name: str = field(default="")
    endpoint: str = field(default="")
    access_key: str = field(default="")
    secret_access_key: str = field(default="")

    @property
    def client(self) -> ObjectStorage:
        return ObjectStorage(
            endpoint=self.endpoint,
            access_key=self.access_key,
            secret_access_key=self.secret_access_key
        )
    
    @property
    def bucket_name(self) -> str:
        return self.name
    
    @classmethod
    def from_env(cls) -> "StorageConfig":
        return cls(**{
            k.lower().replace("objectstorage_", ""): v
            for k, v
            in os.environ.items()
            if k.lower().startswith("objectstorage_")
        })