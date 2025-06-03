# xml_server.py

import time
import xml.etree.ElementTree as ET
from fastapi import FastAPI, Request, Response, HTTPException

app = FastAPI()


def parse_request_xml(body: bytes) -> str:
    """
    Parse incoming XML and return the value of <message>…</message>.
    Raises HTTPException(400) if malformed.
    """
    try:
        root = ET.fromstring(body)
        msg_elem = root.find("message")
        if msg_elem is None or not msg_elem.text:
            raise ValueError("Missing <message> element")
        return msg_elem.text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid XML: {e}")


def build_response_xml(msg: str) -> str:
    """
    Given a text string, build an XML document:
      <Response>
        <message>…</message>
        <timestamp>…</timestamp>
      </Response>
    """
    resp_root = ET.Element("Response")
    ET.SubElement(resp_root, "message").text = msg
    ET.SubElement(resp_root, "timestamp").text = str(time.time())
    return ET.tostring(resp_root, encoding="utf-8", xml_declaration=True).decode("utf-8")


@app.post(
    "/api/xml-chat",
    response_class=Response,
    responses={200: {"content": {"application/xml": {}}}},
)
async def xml_chat(request: Request):
    """
    Expect: Content-Type: application/xml
      <Request>
        <message>…</message>
      </Request>
    Return: Content-Type: application/xml
      <Response>…</Response>
    """
    # 1) Read raw bytes
    body = await request.body()
    # 2) Parse XML
    incoming_msg = parse_request_xml(body)
    # 3) Simulate processing (e.g. echo)
    reply_text = f"XML‐Echo: {incoming_msg}"
    # 4) Build XML response
    xml_data = build_response_xml(reply_text)
    return Response(content=xml_data, media_type="application/xml")
