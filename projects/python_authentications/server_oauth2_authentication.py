"""

Use Case: When delegated access is needed (e.g., logging in with third-party services like Google, GitHub, Facebook). Used in applications where you don't want to share login credentials directly.

Common in: Third-party services, social logins, secure APIs requiring limited access.

Security: Highly secure when implemented correctly with access tokens and refresh tokens.

"""

from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Simulate OAuth clients with client_id and client_secret
clients_db = {
    "client1": {"client_secret": "client1_secret"},
    "client2": {"client_secret": "client2_secret"}
}

# Token storage
tokens_db = {}

def generate_access_token():
    """Generate a secure access token."""
    return secrets.token_hex(16)

@app.route('/oauth/token', methods=['POST'])
def oauth_token():
    """OAuth 2.0 Token endpoint (Client Credentials)."""
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')

    # Validate client credentials
    if client_id in clients_db and clients_db[client_id]["client_secret"] == client_secret:
        token = generate_access_token()
        tokens_db[token] = client_id
        return jsonify({"access_token": token, "token_type": "Bearer", "expires_in": 3600})
    return jsonify({"message": "Invalid client credentials!"}), 401

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Protected route that requires a valid OAuth2 token."""
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"message": "Token is missing!"}), 401

    token = auth_header.split(" ")[1]
    if token in tokens_db:
        return jsonify({"data": f"Secure data accessible by client {tokens_db[token]}!"})
    return jsonify({"message": "Invalid or expired token!"}), 401

if __name__ == "__main__":
    app.run(debug=True)
