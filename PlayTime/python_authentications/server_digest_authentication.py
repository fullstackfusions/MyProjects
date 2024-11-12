"""

Use Case: A more secure alternative to Basic Authentication that hashes the credentials before sending them over the network.

Common in: Older APIs and services, or where higher security is needed without implementing more modern methods like OAuth.

Security: More secure than Basic Authentication, but still considered outdated compared to OAuth or token-based systems.

"""
from flask import Flask, request, jsonify, make_response
import hashlib
import os

app = Flask(__name__)

# Simulate a user database with plain text passwords
users_db = {
    'user1': 'password1',
    'user2': 'password2'
}

# This nonce would normally change every request to prevent replay attacks
NONCE = os.urandom(16).hex()

def hash_password(username, realm, password):
    """Hash user credentials using MD5."""
    ha1 = hashlib.md5(f"{username}:{realm}:{password}".encode('utf-8')).hexdigest()
    return ha1

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Digest Authentication protected route."""
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return digest_challenge()

    auth_parts = {key_value.split('=')[0]: key_value.split('=')[1].strip('"') for key_value in auth_header.replace('Digest ', '').split(', ')}
    username = auth_parts['username']
    realm = auth_parts['realm']
    uri = auth_parts['uri']
    nonce = auth_parts['nonce']
    response = auth_parts['response']

    # Verify the nonce (should match the one sent earlier)
    if nonce != NONCE:
        return digest_challenge()

    # Fetch user password and hash it
    password = users_db.get(username)
    if not password:
        return digest_challenge()

    # Calculate the expected response hash
    ha1 = hash_password(username, realm, password)
    ha2 = hashlib.md5(f"GET:{uri}".encode('utf-8')).hexdigest()
    expected_response = hashlib.md5(f"{ha1}:{nonce}:{ha2}".encode('utf-8')).hexdigest()

    if expected_response == response:
        return jsonify({"data": "Secure data accessible with Digest Authentication!"})
    else:
        return digest_challenge()

def digest_challenge():
    """Respond with Digest Auth challenge."""
    response = make_response('', 401)
    response.headers['WWW-Authenticate'] = f'Digest realm="SecureArea", nonce="{NONCE}", algorithm="MD5", qop="auth"'
    return response

if __name__ == "__main__":
    app.run(debug=True)



import requests
from requests.auth import HTTPDigestAuth

# Define the API endpoint
url = "https://api.example.com/data"

# Digest authentication credentials
username = "myusername"
password = "mypassword"

# Send a GET request with digest authentication
response = requests.get(url, auth=HTTPDigestAuth(username, password))

# Print the response status code and content
print(response.status_code)
print(response.json())
