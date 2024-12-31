"""

Use Case: Common for simple API access where a full-fledged OAuth or token system isn't necessary.

Common in: Public APIs, internal services, SaaS applications, and when there's minimal user interaction.

Security: API keys are generally less secure than token-based authentication, as they can be easily exposed if not handled carefully. Should always be used over HTTPS and rotated regularly.

"""

import secrets
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulate a database of users and their API keys
api_keys_db = {}

def generate_api_key():
    """Generate a secure API key."""
    return secrets.token_hex(32)

@app.route('/register', methods=['POST'])
def register():
    """Register a new user and return an API key."""
    username = request.json.get('username')
    if username in api_keys_db:
        return jsonify({"message": "User already exists!"}), 400
    
    api_key = generate_api_key()
    api_keys_db[username] = api_key
    
    return jsonify({"username": username, "api_key": api_key})

@app.route('/data', methods=['GET'])
def get_data():
    """Authenticate request using API key."""
    api_key = request.headers.get('Authorization')
    if api_key not in api_keys_db.values():
        return jsonify({"message": "Unauthorized!"}), 403

    return jsonify({"data": "Secure data accessible only with a valid API key!"})

if __name__ == "__main__":
    app.run(debug=True)
