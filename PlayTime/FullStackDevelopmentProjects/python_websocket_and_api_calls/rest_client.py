# client.py

import asyncio
import json
from typing import Optional
from pydantic import BaseModel

import httpx
import websockets
from websockets.exceptions import WebSocketException

class TextResponse(BaseModel):
    message: str
    timestamp: float

class APIClient:
    """
    Attempts to keep a WebSocket open at `ws_url`. If that fails (or if it breaks at any point),
    any call to `send_text(...)` will automatically POST to the HTTP endpoint at `api_url`.
    """

    def __init__(self, ws_url: str, api_url: str):
        self.ws_url = ws_url    # e.g. "ws://localhost:8000/ws/chat"
        self.api_url = api_url  # e.g. "http://localhost:8000/api/chat"
        self.ws: Optional[websockets.WebSocketClientProtocol] = None

    async def connect(self) -> None:
        """
        Try to open a WebSocket connection. If it fails, we'll set self.ws = None
        and rely on HTTP fallback from then on.
        """
        try:
            self.ws = await websockets.connect(self.ws_url)
            print("✅ WebSocket connection established.")
        except Exception as e:
            print(f"⚠️  WebSocket connection failed: {e!r}. Will use HTTP instead.")
            self.ws = None

    async def send_text(self, text: str) -> TextResponse:
        """
        1) If there is a healthy WebSocket (self.ws) open, send `{"message": text}` over WS,
           wait for a JSON response, parse it into TextResponse, and return it.
        2) Otherwise, make an HTTP POST to api_url with {"message": text}, parse JSON
           into TextResponse, and return that.
        """
        payload = {"message": text}

        # ——— Try WebSocket first ——————————————————————————————————————————————
        if self.ws:
            try:
                # Send payload over WS
                await self.ws.send(json.dumps(payload))

                # Wait for a JSON reply
                raw = await self.ws.recv()
                data = json.loads(raw)

                # Validate/parse using Pydantic
                return TextResponse(**data)

            except (WebSocketException, ConnectionResetError) as ws_err:
                # If WS fails at any point, drop it and fall back to HTTP
                print(f"⚠️  WebSocket error: {ws_err!r}. Falling back to HTTP.")
                try:
                    await self.ws.close()
                except Exception:
                    pass
                self.ws = None

            except Exception as parse_err:
                # If we got something unexpected over WS, also fall back
                print(f"⚠️  Unexpected WS message/parse error: {parse_err!r}. Using HTTP fallback.")
                try:
                    await self.ws.close()
                except Exception:
                    pass
                self.ws = None

        # ——— Fallback: HTTP POST ————————————————————————————————————————————
        async with httpx.AsyncClient() as client:
            response = await client.post(self.api_url, json=payload)
            response.raise_for_status()
            data = response.json()
            return TextResponse(**data)

    async def close(self) -> None:
        """ Close the WebSocket if it’s open. """
        if self.ws:
            await self.ws.close()
            self.ws = None
            print("🚪 WebSocket closed.")


# ——— Example usage ——————————————————————————————————————————————————————————

async def main():
    """
    In real life, you might import APIClient into your own service or route handler.
    Here, we demo how to connect, send a message, and print the Pydantic‐validated response.
    """

    # 1) Instantiate with your WS and REST URLs:
    client = APIClient(
        ws_url="ws://localhost:8000/ws/chat",
        api_url="http://localhost:8000/api/chat",
    )

    # 2) Try connecting via WebSocket (if your server is up and WS‐capable):
    await client.connect()

    # 3) Send a few sample messages:
    for i in range(3):
        text = f"Hello World! #{i+1}"
        print(f"→ Sending: {text!r}")

        resp: TextResponse = await client.send_text(text)
        # resp is a TextResponse instance, so you can do resp.message, resp.timestamp, etc.
        print(f"⬅️  Got response: {resp.model_dump_json()}\n")

        await asyncio.sleep(0.5)

    # 4) Clean up
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
