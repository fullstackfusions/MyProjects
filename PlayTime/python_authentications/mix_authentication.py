from requests.auth import AuthBase, _basic_auth_str


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
