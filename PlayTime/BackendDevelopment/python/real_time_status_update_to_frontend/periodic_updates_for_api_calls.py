import asyncio
from typing import Optional


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



#suppose one of the function requesting for data using restapi call,
# it takes time to get the data for example 5 minutes,
# then in that case I want to send the status saying "still collecting data..." every minute
# until we move forward with data for next status.

async def get_something(chat_id: str):
    # Launch periodic status task
    status_task = asyncio.create_task(periodic_status(chat_id, "Still collecting data...", interval=60))

    try:
        # Simulate long REST API call (e.g., 5 minutes)
        await asyncio.sleep(300)  # Replace this with your actual async request
        data = "data collected"

    finally:
        status_task.cancel()  # Stop the periodic updates once done

    await send_status(chat_id, "Data collection complete.")
    return data

async def periodic_status(chat_id: str, message: str, interval: int = 60):
    try:
        while True:
            await send_status(chat_id, message)
            await asyncio.sleep(interval)
    except asyncio.CancelledError:
        pass  # Normal expected cancellation

# Helper to send status
async def send_status(chat_id: str, status: str):
    if chat_id in clients:
        await clients[chat_id].send_json({"type": "status", "message": status})
