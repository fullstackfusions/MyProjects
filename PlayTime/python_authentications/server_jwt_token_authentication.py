"""

Use Case: Widely used in APIs and web applications for stateless, token-based authentication. JWTs are self-contained, meaning they carry the necessary information within the token itself.

Common in: RESTful APIs, Single Page Applications (SPAs), mobile apps.

Security: Secure when used with HTTPS and properly managed (e.g., short expiration times, signed tokens). Ensure that sensitive data is not stored in the payload.

"""

# pip install PyJWT
import jwt
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key for encoding and decoding JWT
SECRET_KEY = "your_secret_key"

# Simulate a user database
users_db = {"user1": "password1", "user2": "password2"}

def generate_jwt(username):
    """Generate JWT token for a user."""
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Token expires in 30 minutes
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to get a JWT token."""
    username = request.json.get('username')
    password = request.json.get('password')

    # Verify user credentials
    if username in users_db and users_db[username] == password:
        token = generate_jwt(username)
        return jsonify({"token": token})
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Protected route that requires a valid JWT."""
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Token is missing!"}), 401

    token = auth_header.split(" ")[1]  # Bearer token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"data": f"Secure data accessible by {payload['username']}!"})
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired!"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token!"}), 401

if __name__ == "__main__":
    app.run(debug=True)
