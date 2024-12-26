from marshmallow_dataclass import dataclass
from marshmallow import Schema

@dataclass
class User:
    name: str
    email: str

@dataclass
class Message:
    chatId: str
    user: User
    messageId: str
    role: str
    message: str
    response: str
    timestamp: int

# # Message payload
test_message = Message(chatId="id", user=User(name="name", email="email"), messageId="messageid", role="role", message="message", response="response", timestamp=0)

message_schema = Message.Schema()

serialized_message = message_schema.dumps(test_message)
