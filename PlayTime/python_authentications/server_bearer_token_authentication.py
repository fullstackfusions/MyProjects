"""

Use Case: Most modern APIs that require stateless authentication use token-based authentication. The token is typically issued after successful login or authorization and is passed in each request.

Common in: RESTful APIs, mobile applications, Single Page Applications (SPAs), microservices.

Security: Secure if used with HTTPS and proper token management (e.g., short-lived tokens, refresh tokens).

"""

import secrets
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate a user database
users_db = {"user1": "password1", "user2": "password2"}

# Token database
tokens_db = {}

def generate_token():
    """Generate a secure bearer token."""
    return secrets.token_hex(16)

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint that returns a Bearer token."""
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users_db and users_db[username] == password:
        token = generate_token()
        tokens_db[token] = username
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Protected route that requires a valid Bearer token."""
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Token is missing!"}), 401

    token = auth_header.split(" ")[1]  # Bearer token
    if token in tokens_db:
        return jsonify({"data": f"Secure data accessible by {tokens_db[token]}!"})
    return jsonify({"message": "Invalid token!"}), 401

if __name__ == "__main__":
    app.run(debug=True)
