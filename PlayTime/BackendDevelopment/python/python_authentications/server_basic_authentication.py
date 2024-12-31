"""

Use Case: Simple, straightforward API access where security isn't a huge concern or when used over HTTPS.

Common in: Legacy systems, internal services, or simple web services.

Security: Not very secure on its own since credentials are base64-encoded and can be easily decoded. Should only be used over HTTPS.

"""

import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate a user database
users_db = {"user1": "password1", "user2": "password2"}

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Protected route that requires Basic Authentication."""
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Authorization header is missing!"}), 401

    auth_type, auth_credentials = auth_header.split(" ")
    if auth_type != "Basic":
        return jsonify({"message": "Invalid auth type!"}), 401

    # Decode the credentials (Base64 encoded)
    decoded_credentials = base64.b64decode(auth_credentials).decode("utf-8")
    username, password = decoded_credentials.split(":")

    # Verify credentials
    if username in users_db and users_db[username] == password:
        return jsonify({"data": f"Secure data accessible by {username}!"})
    return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == "__main__":
    app.run(debug=True)
