# xml_pydantic_server.py

import time
import xmltodict
from fastapi import FastAPI, Request, Response, HTTPException
from pydantic import BaseModel

class TextResponse(BaseModel):
    message: str
    timestamp: float

app = FastAPI()

@app.post(
    "/api/xml-validated",
    response_class=Response,
    responses={200: {"content": {"application/xml": {}}}},
)
async def xml_validated(request: Request):
    # 1) Read raw XML
    body = await request.body()
    try:
        parsed = xmltodict.parse(body)  # xml → OrderedDict
        payload = parsed.get("Request")
        if not payload or "message" not in payload:
            raise ValueError("Missing <message> element")
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Invalid XML: {err}")

    # 2) Validate with Pydantic
    try:
        validated = TextResponse(
            message=payload["message"],
            timestamp=time.time(),
        )
    except Exception as val_err:
        raise HTTPException(status_code=422, detail=str(val_err))

    # 3) Build XML response
    response_dict = {"Response": validated.dict()}
    xml_bytes = xmltodict.unparse(response_dict, pretty=True).encode("utf-8")

    return Response(content=xml_bytes, media_type="application/xml")
