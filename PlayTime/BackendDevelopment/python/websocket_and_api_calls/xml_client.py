# xml_client.py

import asyncio
import xml.etree.ElementTree as ET
from typing import Optional

import httpx
import websockets
from websockets.exceptions import WebSocketException


class XMLAPIClient:
    def __init__(self, ws_url: str, api_url: str):
        self.ws_url = ws_url      # e.g. "ws://localhost:8000/ws/chat"
        self.api_url = api_url    # e.g. "http://localhost:8000/api/xml-chat"
        self.ws: Optional[websockets.WebSocketClientProtocol] = None

    async def connect(self) -> None:
        try:
            self.ws = await websockets.connect(self.ws_url)
            print("✅ WebSocket connected.")
        except Exception as e:
            print(f"⚠️  WS connect failed: {e!r}. Will use XML‐HTTP fallback.")
            self.ws = None

    def build_request_xml(self, text: str) -> bytes:
        """
        Wrap text into:
          <Request><message>…</message></Request>
        """
        root = ET.Element("Request")
        ET.SubElement(root, "message").text = text
        return ET.tostring(root, encoding="utf-8", xml_declaration=True)

    def parse_response_xml(self, body: bytes) -> dict:
        """
        Parse:
          <Response><message>…</message><timestamp>…</timestamp></Response>
        Return a simple dict.
        """
        root = ET.fromstring(body)
        msg = root.findtext("message", default="")
        ts = root.findtext("timestamp", default="0")
        return {"message": msg, "timestamp": float(ts)}

    async def send_text(self, text: str) -> dict:
        """
        1) If WS is open: send JSON (as before).
        2) If WS fails or closed: fall back to XML POST.
        """
        # First, try WebSocket
        if self.ws:
            try:
                await self.ws.send(text)  # assuming server expects plain text over WS
                raw = await self.ws.recv()  # get JSON or whatever over WS
                # In many WS‐based chat systems, they still use JSON. Adapt as needed.
                return {"message": raw, "timestamp": 0.0}
            except (WebSocketException, ConnectionResetError):
                print("⚠️  WS broken, falling back to XML‐HTTP.")
                await self.ws.close()
                self.ws = None

        # Fallback: HTTP + XML
        xml_payload = self.build_request_xml(text)
        headers = {"Content-Type": "application/xml"}
        async with httpx.AsyncClient() as client:
            resp = await client.post(self.api_url, content=xml_payload, headers=headers)
            resp.raise_for_status()
            # resp.content is raw XML bytes
            return self.parse_response_xml(resp.content)

    async def close(self) -> None:
        if self.ws:
            await self.ws.close()
            self.ws = None
            print("🚪 WS closed.")


# ————— Example Usage ——————————————————————————————————————————————————

async def main():
    client = XMLAPIClient(
        ws_url="ws://localhost:8000/ws/chat",
        api_url="http://localhost:8000/api/xml-chat",
    )
    await client.connect()

    for i in range(2):
        text = f"Hello XML #{i+1}"
        print(f"→ Sending: {text!r}")
        resp = await client.send_text(text)
        print(f"⬅️  Got response: {resp}\n")
        await asyncio.sleep(0.5)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
