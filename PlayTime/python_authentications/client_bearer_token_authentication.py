"""

Use Case: Most modern APIs that require stateless authentication use token-based authentication. The token is typically issued after successful login or authorization and is passed in each request.

Common in: RESTful APIs, mobile applications, Single Page Applications (SPAs), microservices.

Security: Secure if used with HTTPS and proper token management (e.g., short-lived tokens, refresh tokens).

"""
import requests

# Login and get Bearer token
login_url = "http://localhost:5000/login"
data = {"username": "user1", "password": "password1"}
response = requests.post(login_url, json=data)
token = response.json().get("token")

# Access protected resource
secure_url = "http://localhost:5000/secure-data"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(secure_url, headers=headers)
print(response.json())
