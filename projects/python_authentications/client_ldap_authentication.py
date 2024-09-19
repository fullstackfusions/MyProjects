"""

Use Case: Used in enterprise environments for authentication against a centralized directory of users, such as Active Directory or OpenLDAP.

Common in: Corporate environments, internal applications, enterprise networks.

Security: Secure if used with encrypted connections (e.g., LDAPS). It integrates well with internal user management systems.

"""

import requests

url = "http://localhost:5000/ldap-login"
data = {
    "username": "admin",
    "password": "password123"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())

