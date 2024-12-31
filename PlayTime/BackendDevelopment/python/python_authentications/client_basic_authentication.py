"""

Use Case: Simple, straightforward API access where security isn't a huge concern or when used over HTTPS.

Common in: Legacy systems, internal services, or simple web services.

Security: Not very secure on its own since credentials are base64-encoded and can be easily decoded. Should only be used over HTTPS.

"""
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:5000/secure-data"
username = "user1"
password = "password1"

response = requests.get(url, auth=HTTPBasicAuth(username, password))
print(response.json())
