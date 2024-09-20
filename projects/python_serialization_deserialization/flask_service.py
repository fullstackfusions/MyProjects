# pip install Flask marshmallow requests

from flask import Flask, jsonify, request
from marshmallow import Schema, fields
import requests
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# Apply ProxyFix to ensure Flask trusts the proxy headers
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)


# Marshmallow Schema for serialization and deserialization
class UserSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    age = fields.Int(required=True)

user_schema = UserSchema()

@app.route("/")
def home():
    return "Flask Service is Running"

@app.route('/deserialize', methods=['POST'])
def deserialize_data():
    """Deserialize incoming data from FastAPI"""
    data = request.json
    # Deserialize the data using Marshmallow
    user_data = user_schema.load(data)
    
    print(f"Deserialized Data: {user_data}")

    # Serialize response using Marshmallow
    serialized_data = user_schema.dump(user_data)

    # Send serialized data back to FastAPI
    return jsonify(serialized_data)

@app.route('/send_to_fastapi', methods=['POST'])
def send_to_fastapi():
    """Send serialized data to FastAPI"""
    user = {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30
    }

    # Serialize the data using Marshmallow
    serialized_user = user_schema.dump(user)
    
    # Send the serialized data to FastAPI
    response = requests.post("http://fastapi_service:8000/deserialize", json=serialized_user)
    
    return jsonify(response.json()), response.status_code
    # return response.json()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


# python flask_service.py
# Flask will run on http://localhost:5000.


# curl command for deserialization data:
# curl -X 'POST' \
#   'http://localhost:5001/deserialize' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "id": 0,
#   "name": "string",
#   "email": "user@example.com",
#   "age": 0
# }'


# curl command for serialization data:
# curl -X POST http://localhost:5001/send_to_fastapi