# pip install fastapi pydantic uvicorn requests
# pip install email-validator or pip install "pydantic[email]"

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import requests

app = FastAPI()


@app.get("/")
def home():
    return "FastAPI Service is Running"

# Pydantic Model for serialization and deserialization
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

@app.post("/deserialize")
async def deserialize_data(user: User):
    """Deserialize incoming data from Flask"""
    print(f"Deserialized Data: {user}")

    # Serialize the response using Pydantic
    serialized_user = user.model_dump()

    return serialized_user

@app.post("/send_to_flask")
async def send_to_flask():
    """Send serialized data to Flask"""
    user = {
        "id": 1,
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "age": 28
    }

    # Serialize the data using Pydantic
    user_model = User(**user)
    serialized_user = user_model.model_dump()

    # Send serialized data to Flask for deserialization
    response = requests.post("http://flask_service:5000/deserialize", json=serialized_user)
    
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# uvicorn src/fastapi_service:app --reload
# FastAPI will run on http://localhost:8000.


# curl command for deserialization data:
# curl -X 'POST' \
#   'http://localhost:8000/deserialize' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "id": 0,
#   "name": "string",
#   "email": "user@example.com",
#   "age": 0
# }'


# curl command for serialization data:
# curl -X POST http://localhost:8000/send_to_flask