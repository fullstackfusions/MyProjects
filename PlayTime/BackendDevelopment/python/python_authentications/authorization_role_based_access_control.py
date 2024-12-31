"""

Role-Based Access Control (RBAC): The system checks the user's role (e.g., admin, user, guest) and grants or denies access based on permissions associated with that role.

Example: The user accesses a specific route or resource, and the system checks whether the user is authorized to perform that action based on the token's claims (authorization).

"""

import jwt
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key to sign JWT
SECRET_KEY = "your_secret_key"

# Simulated user database with roles
users_db = {
    "admin_user": {"password": "adminpass", "role": "admin"},
    "regular_user": {"password": "userpass", "role": "user"}
}

# Generate JWT with role and expiration time
def generate_jwt(username, role):
    payload = {
        "username": username,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)  # Token expires in 30 seconds
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Function to check user role
def check_user_role(token, required_role):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_role = payload.get("role")
        if user_role == required_role:
            return True
        else:
            return False
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint that generates JWT with role-based access."""
    username = request.json.get('username')
    password = request.json.get('password')

    user = users_db.get(username)
    if user and user["password"] == password:
        token = generate_jwt(username, user["role"])
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/admin', methods=['GET'])
def admin_resource():
    """Protected admin route, accessible only by users with admin role."""
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Authorization header is missing!"}), 401

    token = auth_header.split(" ")[1]  # Get the token from "Bearer <token>"
    
    role_check = check_user_role(token, "admin")
    
    if role_check == True:
        return jsonify({"data": "Welcome, admin! You have access to this resource."}), 200
    elif role_check == "Token expired":
        return jsonify({"message": "Token has expired!"}), 401
    elif role_check == "Invalid token":
        return jsonify({"message": "Invalid token!"}), 401
    else:
        return jsonify({"message": "You are not authorized to access this resource!"}), 403

@app.route('/user', methods=['GET'])
def user_resource():
    """Protected user route, accessible by both admin and regular users."""
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Authorization header is missing!"}), 401

    token = auth_header.split(" ")[1]
    
    role_check = check_user_role(token, "user")
    
    if role_check == True:
        return jsonify({"data": "Welcome! You have access to this user resource."}), 200
    elif role_check == "Token expired":
        return jsonify({"message": "Token has expired!"}), 401
    elif role_check == "Invalid token":
        return jsonify({"message": "Invalid token!"}), 401
    else:
        return jsonify({"message": "You are not authorized to access this resource!"}), 403

if __name__ == "__main__":
    app.run(debug=True)
