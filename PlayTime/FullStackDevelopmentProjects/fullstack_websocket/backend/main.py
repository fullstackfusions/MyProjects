from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager

app = FastAPI()
connected_clients = set()

# Lifespan handler (no terminal input needed now)
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield  # No startup/shutdown tasks needed for now

app = FastAPI(lifespan=lifespan)

# Function to process messages (for testing, just prepend "Processed: ")
async def process_message(message: str) -> str:
    processed = f"Processed: {message}"
    # print(f"Processed message: {processed}")  # For debugging
    return processed

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    print(f"Client connected. Total clients: {len(connected_clients)}")
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message: {data}")
            # Process the message
            processed_message = await process_message(data)
            # Send processed message back to all clients
            for client in list(connected_clients):
                try:
                    await client.send_text(processed_message)
                    print(f"Sent processed message to client: {processed_message}")
                except Exception as e:
                    print(f"Failed to send to client: {e}")
                    connected_clients.remove(client)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connected_clients.remove(websocket)
        print(f"Client disconnected. Total clients: {len(connected_clients)}")

@app.get("/")
async def get():
    return HTMLResponse("FastAPI Backend Running")
