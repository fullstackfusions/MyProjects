"""

This approach with Session is considerably better approach compared to simple request.

In this we have setup the adapter to have verification, proxies check and timeout check with retry options.

Also implemented few authentication systems like basic authentication, token authentication and oauth2 authentication.

"""

import logging
import requests
from abc import abstractmethod
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any
from requests.auth import AuthBase, _basic_auth_str

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Authentication Classes
class APICredential(AuthBase):
    pass


class APIBasicCredential(APICredential):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
    
    def __call__(self, request, *args, **kwargs):
        request.headers["Authorization"] = _basic_auth_str(self.username, self.password)
        return request


class APITokenCredential(APICredential):
    def __init__(self, token) -> None:
        self.token = token
    
    def __call__(self, request, *args, **kwargs):
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request


class APIOAuth2Credential(APICredential):
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
    
    def __call__(self, request, *args, **kwargs):
        request.headers["Authorization"] = _basic_auth_str(self.client_id, self.client_secret)
        return request


# Enums
from enum import Enum

class HTTPScheme(str, Enum):
    HTTP = 'http'
    HTTPS = 'https'

    def __str__(self) -> str:
        return self.value


class HTTPPort(int, Enum):
    HTTP = 80
    HTTPS = 443  # Corrected to the default HTTPS port

    def __int__(self) -> int:
        return self.value


class HTTPVerify(bool, Enum):
    VERIFY = True
    NO_VERIFY = False


# Custom Adapter class
class CustomHTTPAdapter(HTTPAdapter):
    """
    Custom HTTPAdapter to handle retries, timeouts, and no proxy settings.
    """

    def __init__(self, timeout: int = 5, verify: bool = True, no_proxy: Optional[str] = None, *args, **kwargs):
        self.timeout = timeout
        self.verify = verify
        self.no_proxy = no_proxy
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        """
        Override the send method to inject custom behavior.
        """
        kwargs['timeout'] = kwargs.get('timeout', self.timeout)
        kwargs['verify'] = self.verify

        # Handle no_proxy if specified
        if self.no_proxy:
            kwargs['proxies'] = {"http": None, "https": None}

        return super().send(request, **kwargs)


# API Client class
class APIClient:
    """
    Base API client to manage session and API requests.
    """

    def __init__(self,
                 credential: APICredential,
                 server: str,
                 port: int = HTTPPort.HTTPS,
                 scheme: HTTPScheme = HTTPScheme.HTTPS,
                 timeout: int = 5,
                 verify: bool = True,
                 proxy: bool = False
                 ) -> None:
        
        self.credential = credential
        self.server = server
        self.port = port
        self.scheme = scheme
        self.timeout = timeout
        self.verify = verify
    
        
        self.url = f"{self.scheme}://{self.server}:{int(self.port)}"
        
        self.proxy = proxy
        self.no_proxy = None

        if not self.proxy:
            self.session.proxies.update(
                dict(
                    no=self.server
                )
            )
            self.no_proxy = self.server
        
        self.session = requests.Session()
        self.session.verify = self.verify

        adapter = CustomHTTPAdapter(
            max_retries=Retry(
                total=3,
                connect=3,
                read=3,
                redirect=3,
                status=3,
                backoff_factor=15,
                status_forcelist=[429, 500, 502, 503, 504],
            ),
            timeout=self.timeout,
            verify=self.session.verify,
            no_proxy=self.no_proxy
        )
        
        # Mount the adapter to handle all http and https requests
        self.session.mount(
            prefix=self.url,
            adapter=adapter
        )

        # Add credentials to the session
        self.session.auth = self.credential

    def request(self, *args, **kwargs) -> Optional[requests.Response]:
        """
        Perform a request using the session.
        """
        kwargs.setdefault("timeout", self.timeout)
        kwargs.setdefault("verify", self.session.verify)
        kwargs.setdefault("proxies", self.session.proxies)


        try:
            response = self.session.request(*args, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logger.error(f"Error during request: {e}")
            raise

    @abstractmethod
    def _authenticate(self) -> None:
        raise NotImplementedError


# Example Subclass for a Specific API
class ExampleAPIClient(APIClient):
    """
    Example API client for a specific API.
    """

    def __init__(self, credential: APICredential, server: str) -> None:
        super().__init__(credential, server)
        self._url_api = f"{self.url}/api"
        self._token = None
        self._token_refresh_time = datetime.now(timezone.utc)
        self._token_expiry_time = datetime.now(timezone.utc)

        self._authenticate()

    def _authenticate(self) -> None:
        if self._is_token_expired() or self._is_token_refresh_due():
            response = self.request(
                method="POST",
                url=f"{self._url_api}/login",
                json={"username": self.credential.username, "password": self.credential.password}
            )
            if response:
                response_json = response.json()
                self._token = response_json.get('token')
                # Update token expiry times
                self._token_refresh_time = datetime.now(timezone.utc) + timedelta(minutes=10)
                self._token_expiry_time = datetime.now(timezone.utc) + timedelta(hours=24)

    def _is_token_expired(self) -> bool:
        return datetime.now(timezone.utc) > self._token_expiry_time

    def _is_token_refresh_due(self) -> bool:
        return datetime.now(timezone.utc) > self._token_refresh_time

    def fetch_data(self, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Fetch data from the example API endpoint.
        """
        response = self.request(method="GET", url='/data', params=params)
        return response.json() if response else None

    def fetch_paginated_data(self, params: dict):
        # here we are assuming the page limits are defined inside url or in params
        response = self.request(
            method="POST",
            url="some url",
            headers=params["headers"],
            auth=params["auth"], # can be basic auth, token, or oauth2
            json=params["params"],
            verify=True 
        )
        return response



