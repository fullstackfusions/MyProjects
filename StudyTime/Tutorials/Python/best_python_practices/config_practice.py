# Configuration or fetching any environment variable approach:
import logging
import os
import time
import requests
from typing import Dict, Any
from dataclasses import field
from marshmallow_dataclass import dataclass
from mongoengine import connect


@dataclass
class OpenAIConfig:
    client_id: str
    client_secret: str
    oauth_api: str
    openai_api_base: str
    _token: str = field(default=None)
    _token_expiry: int = field(default=0)

    def _get_new_token(self) -> str:
        headers = {"Content-Type": "application/x-www-from-urlencoded"}
        oauth_gen_data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": "read"
        }
        oauth_token_response = requests.post(url=self.oauth_api, data=oauth_gen_data, headers=headers, verify=False)
        if oauth_token_response.ok:
            token_data = oauth_token_response.json()
            self._token = token_data["access_token"]
            self._token_expiry = time.time() + token_data.get("expires_in", 3600)
        else:
            raise Exception("Failed to get apigee oauth token")

    @property
    def openai_api(self) -> str:
        return self.openai_api_base

    @property
    def token(self) -> str:
        if self._token is None or time.time() > self._token_expiry:
            self._get_new_token()
        return self._token

    @classmethod
    def from_env(cls) -> 'OpenAIConfig':
        return cls(**{
            k.lower().replace('openai_', ''): v
            for k, v
            in os.environ.items()
            if 'openai_' in k.lower()
        })


@dataclass
class EmailConfig:
    username: str
    password: str
    server: str

    @property
    def client(self):
        return EmailConfig(
            username=self.username,
            password=self.password,
            server=self.server,
        )

    @classmethod
    def from_env(cls):
        return cls(**{
            k.lower().replace('email_', ''): v
            for k, v
            in os.environ.items()
            if 'email_' in k.lower()
        })

    def send_email(self, response, *args, **kwargs) -> bool:
        try:
            self.client.message(
                subject="",
                body="",
                to="",
                cc="",
                attachments=[]
            ).send_and_save()
            return True
        except:
            logging.exception()

# Following setup is used in VaultConfig
@dataclass
class APICredentialBasic:
    username: str
    password: str

class Vault:
    def __init__(self, credential: APICredentialBasic, server: str):
        self.credential = credential
        self.server = server

    def authenticate(self):
        # Example method to demonstrate usage
        print(f"Authenticating to {self.server} with username {self.credential.username}")


@dataclass
class VaultConfig:
    server: str
    username: str
    password: str
    secret_path: str

    @property
    def client(self) -> Vault:
        return Vault(
            credential = APICredentialBasic(
                username=self.username,
                password=self.password
            ),
            server=self.server
        )

    @property
    def secrets(self) -> Dict[Any, Any]:
        return self.client.get_secret(self.secret_path)

    @classmethod
    def from_env(cls) -> 'VaultConfig':
        return cls(**{
            k.lower().replace('vault_', ''): v
            for k, v
            in os.environ.items()
            if 'vault_' in k.lower()
        })

@dataclass
class StorageConfig:
    name: str
    endpoint: str
    access_key: str
    secret_access_key: str

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
    def from_env(cls) -> 'StorageConfig':
        return cls(**{
            k.lower().replace('objstorage_', ''): v
            for k, v
            in os.environ.items()
            if 'objstorage_' in k.lower()
        })


@dataclass
class MongoConfig:
    host: str
    port: str
    username: str
    password: str
    db: str

    @property
    def client(self) -> None:
        connect(
            host=self.host,
            port=int(self.port),
            username=self.username,
            password=self.password,
            authSource="$external",
            authMechanism="PLAIN",
            db=self.db
        )

    @classmethod
    def from_env(cls) -> 'MongoConfig':
        return cls(**{
            k.lower().replace('mongo_', ''): v
            for k, v
            in os.environ.items()
            if 'mongo_' in k.lower()
        })

@dataclass
class Config:
    vault: VaultConfig = field(default_factory=VaultConfig.from_env)
    mongo: MongoConfig = field(default_factory=MongoConfig.from_env)
    email: EmailConfig = field(default_factory=EmailConfig.from_env)
    storage: StorageConfig = field(default_factory=StorageConfig.from_env)
