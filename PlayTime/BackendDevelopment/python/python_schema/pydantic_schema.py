from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    name: str
    email: str

class Response(BaseModel):
    status: str
    code: int

class TextResponse(BaseModel):
    text: str

class TemplateResponse(BaseModel):
    template_id: str
    data: dict

class Message(BaseModel):
    chatId: str
    user: User
    messageId: str
    role: str
    message: str
    response: Union[str, Response, TextResponse, TemplateResponse]
    timestamp: int


# Example message with a standard response
test_message_response = Message(
    chatId="id",
    user=User(name="name", email="email"),
    messageId="messageid",
    role="role",
    message="hello",
    response=Response(status="ok", code=200),
    timestamp=0
)

# Example message with a text response
test_message_text = Message(
    chatId="id",
    user=User(name="name", email="email"),
    messageId="messageid",
    role="role",
    message="hello",
    response=TextResponse(text="Hello, world!"),
    timestamp=0
)

# Example message with a template response
test_message_template = Message(
    chatId="id",
    user=User(name="name", email="email"),
    messageId="messageid",
    role="role",
    message="hello",
    response=TemplateResponse(template_id="template123", data={"key": "value"}),
    timestamp=0
)

# print(test_message_response.model_dump_json())
# print(test_message_text.model_dump_json())
# print(test_message_template.model_dump_json())
