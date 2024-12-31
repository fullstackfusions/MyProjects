"""

Use Case: A more secure alternative to Basic Authentication that hashes the credentials before sending them over the network.

Common in: Older APIs and services, or where higher security is needed without implementing more modern methods like OAuth.

Security: More secure than Basic Authentication, but still considered outdated compared to OAuth or token-based systems.

"""
import requests
from requests.auth import HTTPDigestAuth

url = "http://localhost:5000/secure-data"
username = "user1"
password = "password1"

response = requests.get(url, auth=HTTPDigestAuth(username, password))
print(response.status_code)
print(response.json() if response.status_code == 200 else response.text)
