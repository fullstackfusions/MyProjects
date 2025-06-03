# xml_pydantic_client_with_model.py

import asyncio
import xml.etree.ElementTree as ET
import xmltodict
import httpx
import websockets
from websockets.exceptions import WebSocketException
from typing import Optional

from pydantic import BaseModel


# ─── 1) Define the Pydantic model (must match server’s TextResponse exactly) ─────────────
class TextResponse(BaseModel):
    message: str
    timestamp: float


# ─── 2) XML + WS client with Pydantic validation ─────────────────────────────────────────
class XMLAPIClient:
    def __init__(self, ws_url: str, api_url: str):
        self.ws_url = ws_url      # e.g. "ws://localhost:8000/ws/chat"
        self.api_url = api_url    # e.g. "http://localhost:8000/api/xml-validated"
        self.ws: Optional[websockets.WebSocketClientProtocol] = None

    async def connect(self) -> None:
        try:
            self.ws = await websockets.connect(self.ws_url)
            print("✅ WebSocket connected.")
        except Exception as e:
            print(f"⚠️  WS connect failed: {e!r}. Using XML‐HTTP fallback.")
            self.ws = None

    def build_request_xml(self, text: str) -> bytes:
        """
        Construct:
          <?xml version='1.0' encoding='utf-8'?>
          <Request>
            <message>…</message>
          </Request>
        """
        root = ET.Element("Request")
        msg_elem = ET.SubElement(root, "message")
        msg_elem.text = text
        return ET.tostring(root, encoding="utf-8", xml_declaration=True)

    def parse_response_xml(self, body: bytes) -> TextResponse:
        """
        1) Parse raw XML into a dict via xmltodict.
        2) Feed that dict into Pydantic TextResponse for validation.
        """
        parsed = xmltodict.parse(body)
        resp_dict = parsed.get("Response", {})
        # Now resp_dict should be {"message": "...", "timestamp": "123456.789"}
        # Convert timestamp to float (xmltodict leaves it as string)
        try:
            resp_dict["timestamp"] = float(resp_dict.get("timestamp", 0))
        except ValueError:
            resp_dict["timestamp"] = 0.0

        # Instantiate Pydantic model
        return TextResponse(**resp_dict)

    async def send_text(self, text: str) -> TextResponse:
        # — Try WebSocket first (assuming server returns JSON over WS) —
        if self.ws:
            try:
                await self.ws.send(text)
                raw = await self.ws.recv()
                print("📡 Received over WS (raw):", raw)
                # If your WS response is JSON matching TextResponse, parse it:
                try:
                    return TextResponse.model_dump(raw)
                except Exception as e:
                    print("⚠️  WS JSON parse failed:", e)
                    # fall back to XML below
                    await self.ws.close()
                    self.ws = None
                # If parse_raw fails, we treat it as WS broken:
            except (WebSocketException, ConnectionResetError) as ws_err:
                print(f"⚠️  WS error {ws_err!r}, falling back to HTTP.")
                try:
                    await self.ws.close()
                except Exception:
                    pass
                self.ws = None

        # — Fallback: HTTP + XML —
        xml_payload = self.build_request_xml(text)
        headers = {"Content-Type": "application/xml"}
        async with httpx.AsyncClient() as client:
            resp = await client.post(self.api_url, content=xml_payload, headers=headers)
            resp.raise_for_status()
            print("📡 Received over HTTP (raw XML):", resp.text)
            # Parse & validate via Pydantic
            return self.parse_response_xml(resp.content)

    async def close(self) -> None:
        if self.ws:
            await self.ws.close()
            self.ws = None
            print("🚪 WS closed.")


# ─── 3) Example run ─────────────────────────────────────────────────────────────────────
async def main():
    client = XMLAPIClient(
        ws_url="ws://localhost:8000/ws/chat",
        api_url="http://localhost:8000/api/xml-validated",
    )
    await client.connect()

    for i in range(2):
        text = f"Test-XML #{i+1}"
        print(f"→ Sending: {text!r}")
        try:
            resp_model = await client.send_text(text)
            # resp_model is a TextResponse instance
            print(f"⬅️  Validated response: {resp_model.model_dump_json()}\n")
        except Exception as e:
            print("❌ Error parsing response:", e)
        await asyncio.sleep(0.5)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
