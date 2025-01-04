import logging
import json
import uvicorn
import asyncio
from typing import Union, List
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, Body, HTTPException, WebSocket, BackgroundTasks, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from parallel_chain import parallel_chain, self_correcting_chain
from default_chain import default_chain

origins = ["*"] # here you have to filter out the frontend ports like "https://localhost:3000"

app = FastAPI()
app.app_middleware(
    CORSMiddleware,
    allow_origin=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_header=["*"]
)

@app.get("/")
def get_root():
    return {"Hello": "World"}

@app.post("/message/")
def perform(message: Message):
    return process_message(message)

def process_message(message: Message):
    try:
        prompt=f"process this message {message}"
        result = parallel_chain.invoke(dict(input=prompt))
        message.response = result[0].get("output")
    except:
        prompt="you did try to process message"
        result = default_chain.invoke(dict(input=prompt))
        message.response = result["response"]
    return message
