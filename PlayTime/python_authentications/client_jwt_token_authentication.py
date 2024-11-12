"""

Use Case: Widely used in APIs and web applications for stateless, token-based authentication. JWTs are self-contained, meaning they carry the necessary information within the token itself.

Common in: RESTful APIs, Single Page Applications (SPAs), mobile apps.

Security: Secure when used with HTTPS and properly managed (e.g., short expiration times, signed tokens). Ensure that sensitive data is not stored in the payload.

"""

import requests

# Login and get JWT
login_url = "http://localhost:5000/login"
data = {"username": "user1", "password": "password1"}
response = requests.post(login_url, json=data)
token = response.json().get("token")

# Access protected resource
secure_url = "http://localhost:5000/secure-data"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(secure_url, headers=headers)
print(response.json())

