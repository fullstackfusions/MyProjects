## Explanation:

### MongoDB Connection:

We use motor to create an asynchronous MongoDB client that connects to the database todo_db and the collection todo_collection.

### Pydantic Models:

#### TodoItem:

This is the main Pydantic model for a to-do item with fields header (string), data (a dictionary to track items and their statuses), and an optional description.

#### TodoItemUpdate:

This is the Pydantic model used for partial updates. Fields are optional.

#### TodoItemDB:

Extends TodoItem and includes an \_id field, which is the MongoDB ObjectId.

### CRUD Operations:

**Create (POST /todo)**: Adds a new to-do item.
**Read All (GET /todos)**: Returns a list of all to-do items.
**Read One (GET /todo/{id})**: Returns a single to-do item by ID.
**Update (PUT /todo/{id})**: Updates a to-do item by ID.
**Delete (DELETE /todo/{id})**: Deletes a to-do item by ID.

## Running the FastAPI Application

1. Make sure MongoDB is running locally: You need a running MongoDB instance. You can start MongoDB locally using Docker or a local MongoDB installation.

`docker run -d -p 27017:27017 --name mongodb mongo`

2. Run the FastAPI application: Save the script as app.py and run the FastAPI application using uvicorn.

`uvicorn app:app --reload`

> FastAPI will start the server on http://127.0.0.1:8000.

## Testing the API

You can test the FastAPI endpoints using Postman, cURL, or directly through FastAPI's interactive API docs.

1. Add a To-Do Item:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'Content-Type: application/json' \
  -d '{
  "header": "Shopping List",
  "data": {
    "Buy milk": false,
    "Buy bread": true
  },
  "description": "List of items to buy"
}'
```

2. Get All To-Do Items:

```bash
curl -X 'GET' 'http://127.0.0.1:8000/todos'
```

3. Update a To-Do Item:

```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/todo/<id>' \
  -H 'Content-Type: application/json' \
  -d '{
  "header": "Updated Shopping List",
  "data": {
    "Buy milk": true
  }
}'
```

4. Delete a To-Do Item:

```bash
curl -X 'DELETE' 'http://127.0.0.1:8000/todo/<id>'
```

## MongoDB Setup and Collections

1. Database: todo_db
2. Collection: todo_collection
3. Each to-do item is stored in the MongoDB collection with the fields header, data, and description. The MongoDB ObjectId is used as the unique identifier for each to-do item.

## Containerized and Deployment Process:

### Run FastAPI application:

- **Build the FastAPI application container**
  `docker build -f Dockerfile-todo -t fastapi-todo-app .`

- **Run the FastAPI application container**
  `docker run -d --name fastapi-app -p 8000:8000 fastapi-todo-app`

### Run Streamlit application:

- **Build the Streamlit UI container**
  `docker build -f Dockerfile-streamlit -t streamlit-todo-app .`

- **Run the Streamlit UI container**
  `docker run -d --name streamlit-app -p 8501:8501 streamlit-todo-app`

### Kubernetes setup and test

1. **User minikube Docker Environment**:
   `eval $(minikube -p minikube docker-env)`

2. **Build Docker Images Inside Minikube**:
   `docker build -f Dockerfile-todo -t fastapi-todo-app .`
   `docker build -f Dockerfile-streamlit -t streamlit-todo-app .`

3. **Verify locally build images**:
   `docker images`

4. **Apply Kubernetes configuration**:
   `kubectl apply -f kubernetes-deploy.yaml`

5. **Verify Deployments**:
   `kubectl get pods`

6. **Expose Services**:
   `minikube service todo-service --url`

7. **Access applications**:
   FastAPI: The FastAPI API should be accessible at http://<minikube-ip>:<node-port> (e.g., http://192.168.49.2:30777)
   Streamlit: The Streamlit UI should be accessible at http://<minikube-ip>:<node-port> (e.g., http://192.168.49.2:30778)

8. **Check pod logs**:
   `kubectl logs <pod-name> -c fastapi-todo`
   `kubectl logs <pod-name> -c streamlit-todo`

9. **Run container interactively**:

   - to check the logs in interactive mode:
     `docker run -it fastapi-todo-app /bin/sh`

10. **Check the service configuration**:
    `kubectl describe svc todo-service`

11. **Check pod status and description**:
    `kubectl describe pod <pod-name>`

12. **After applying any changes restart minikube**:
    - Minikube is like Docker Daemon, it should be running in order to build any docker image
      `minikube stop`
      `minikube start`
