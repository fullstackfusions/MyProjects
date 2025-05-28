from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from typing import Dict
from pydantic import BaseModel
import uuid

app = FastAPI()

# Store connected clients
clients: Dict[str, WebSocket] = {}

class Message(BaseModel):
    chatId: str
    messageId: str
    user: dict
    role: str
    request_payload: dict
    response_payload: dict | None = None
    timestamp: int

# WebSocket endpoint
@app.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str):
    await websocket.accept()
    clients[chat_id] = websocket
    try:
        while True:
            await websocket.receive_text()  # no-op read to keep alive
    except WebSocketDisconnect:
        del clients[chat_id]

# REST endpoint
@app.post("/message")
async def message_handler(message: Message):
    await send_status(message.chatId, "Message received. Starting processing...")

    result = await process_message(message)

    # Final message result
    return JSONResponse(content=result)

# Helper to send status
async def send_status(chat_id: str, status: str):
    if chat_id in clients:
        await clients[chat_id].send_json({"type": "status", "message": status})

# Main processing logic
async def process_message(message: Message):
    await send_status(message.chatId, "Processing started...")

    s = await get_something(message.chatId)
    await send_status(message.chatId, "Performing transformation...")

    transformed = {"response_payload": {"text": f"Transformed {s}"}}
    return transformed

# Simulated sub-call
async def get_something(chat_id: str):
    await send_status(chat_id, "Getting something...")
    return "some data"
