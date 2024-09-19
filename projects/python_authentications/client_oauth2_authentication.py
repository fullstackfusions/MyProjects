"""

Use Case: When delegated access is needed (e.g., logging in with third-party services like Google, GitHub, Facebook). Used in applications where you don't want to share login credentials directly.

Common in: Third-party services, social logins, secure APIs requiring limited access.

Security: Highly secure when implemented correctly with access tokens and refresh tokens.

"""
import requests

# Get OAuth2 token
token_url = "http://localhost:5000/oauth/token"
data = {"client_id": "client1", "client_secret": "client1_secret"}
response = requests.post(token_url, data=data)
token = response.json().get("access_token")

# Access protected resource
secure_url = "http://localhost:5000/secure-data"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(secure_url, headers=headers)
print(response.json())
