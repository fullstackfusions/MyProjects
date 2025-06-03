# server.py

import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Dict
import time

# ─── The Pydantic schema must match models.TextResponse exactly ──────────────
# (In real life, you’d share this file or copy it so frontend + backend stay in sync.)

class TextResponse(BaseModel):
    message: str
    timestamp: float


# ─── Simple in‐memory “echo bot” for WebSocket connections ───────────────────────
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, client_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: str):
        self.active_connections.pop(client_id, None)

    async def send_text_response(self, client_id: str, text: str):
        """
        Build a TextResponse model and send it back over WebSocket.
        """
        resp = TextResponse(message=text, timestamp=time.time())
        await self.active_connections[client_id].send_json(resp.dict())


# ─── FastAPI app ───────────────────────────────────────────────────────────────
app = FastAPI()

# (Optional) If you’re calling from a browser-based frontend on a different port:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = ConnectionManager()


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    """
    WebSocket endpoint at ws://<host>:8000/ws/chat
    We assign each connection a dummy client_id (e.g. "client1") for simplicity.
    Here, the server just echoes back every message with a timestamp.
    """
    client_id = "client1"
    await manager.connect(client_id, websocket)

    try:
        while True:
            data = await websocket.receive_json()
            # Suppose the client always sends {"message": "..."}
            user_msg = data.get("message", "<no message>")
            # Echo back with timestamp:
            await manager.send_text_response(client_id, f"Echo: {user_msg}")
    except WebSocketDisconnect:
        manager.disconnect(client_id)
    except Exception as e:
        manager.disconnect(client_id)


@app.post("/api/chat", response_model=TextResponse)
async def http_chat(payload: Dict[str, str]):
    """
    HTTP POST endpoint at http://<host>:8000/api/chat
    Accepts JSON: {"message": "..."}
    Returns a TextResponse with an echo.
    """
    if "message" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'message' field")

    user_msg = payload["message"]
    # Simulate some processing delay
    await asyncio.sleep(0.1)
    return TextResponse(message=f"HTTP-Echo: {user_msg}", timestamp=time.time())
