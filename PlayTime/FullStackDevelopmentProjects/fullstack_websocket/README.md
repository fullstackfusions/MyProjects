I'll guide you through creating a project with a React + TypeScript frontend using Vite and a FastAPI backend with WebSocket support. Here's a step-by-step implementation:

### Project Structure
```
project-root/
├── frontend/
│   ├── src/
│   └── package.json
├── backend/
│   ├── main.py
│   └── requirements.txt
```

### 1. Frontend Setup (Vite + React + TypeScript)

#### Step 1: Create Frontend
```bash
npm create vite@latest my-react-app --template react-ts
cd frontend
npm install
```

#### Step 2: Install WebSocket Dependency
```bash
cd frontend
npm install ws
```


#### step 3: Run Frontend
```bash
cd frontend
npm run dev
```
- Frontend will run on `http://localhost:5173` by default


### 2. Backend Setup (FastAPI)

#### Step 1: Create Backend Directory
```bash
mkdir backend
cd backend
```

#### Step 2: Create Virtual Environment and Install FastAPI
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install fastapi uvicorn websockets
```

#### Step 3: Create `requirements.txt`
```
fastapi
uvicorn
websockets
```

#### step 3: Run Backend
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload --port 8000
```
- Backend will run on `http://localhost:8000`
- WebSocket endpoint will be available at `ws://localhost:8000/ws`


### How It Works
1. The frontend connects to the backend WebSocket at `ws://localhost:8000/ws`
2. When you type a message and click "Send", it’s sent to the backend
3. The backend broadcasts the message to all connected clients
4. All connected frontend instances display the received messages

### Notes
- Ensure both frontend and backend are running simultaneously in separate terminals
- The WebSocket connection is basic; you might want to add error handling or reconnection logic for production
- CORS is not configured here; for production, add CORS middleware to FastAPI if the frontend is hosted on a different domain
