"""

- OAuth2PasswordBearer is used to define the token URL.
- The login endpoint authenticates the user and returns an access token. The login endpoint creates and returns the JWT upon successful authentication.
- create_access_token generates a JWT with an expiration time and includes scopes in the JWT.
- The get_current_user function decodes the JWT and retrieves the user. get_current_user also checks if the required scopes are present in the JWT.
- oauth2_scheme defines the available scopes.
- The read_users_me endpoint retrieves the current user using the access token.

"""

import jwt
import logging
from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from fastapi import Depends, FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from mongodb import MongoDBHandler


logger = logging.getLogger(__name__)


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
mongodb_handler = MongoDBHandler()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", scopes={"me": "Read information about the current user"})

# Update the User models
class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str
    disabled: Optional[bool] = False

# Pydantic Model for To-Do Item
class TodoItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoItem(TodoItemBase):
    id: int
    created_by: Optional[str] = Field(None, exclude=True)  # Exclude from user input
    created_at: Optional[datetime] = Field(default_factory=datetime, exclude=True)  # Auto-populate with current time
    updated_at: Optional[datetime] = Field(default_factory=datetime, exclude=True)

    class Config:
        orm_mode = True  # Enables using Pydantic model with ORMs, like MongoDB
        extra = 'forbid'  # Prevents users from adding extra fields


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# To test without database
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": pwd_context.hash("secret"),
        "disabled": False,
    }
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# def get_user_from_fake_db(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         print(user_dict)
#         return UserInDB(**user_dict)

async def get_user(username: str):
    user_dict = await mongodb_handler.get_user_by_username(username)
    if user_dict:
        return UserInDB(**user_dict)


async def authenticate_user(username: str, password: str):
    # user = get_user_from_fake_db(fake_db, username)
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, scopes: list, expires_delta: timedelta = None):
    to_encode = data.copy()
    to_encode.update({"scopes": scopes})
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, scopes=["me"], expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Implement the /register endpoint
@app.post("/register")
async def register(user: UserCreate = Body(...)):
    # Check if the username already exists
    existing_user = await mongodb_handler.get_user_data(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = pwd_context.hash(user.password)
    user_data = user.model_dump()
    user_data['hashed_password'] = hashed_password
    del user_data['password']
    user_data['disabled'] = False  # Set default disabled status
    result = await mongodb_handler.insert_user_data(user_data)
    if result.inserted_id:
        return {"message": "User registered successfully"}
    else:
        raise HTTPException(status_code=500, detail="User registration failed")

async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        token_scopes = payload.get("scopes", [])
        if username is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_scopes:
                raise HTTPException(
                    status_code=403,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": "Bearer"},
                )
    except jwt.PyJWTError:
        raise credentials_exception
    # user = get_user_from_fake_db(fake_users_db, username)
    user = get_user(username=username)
    if user is None:
        raise credentials_exception
    return user


# Assign a numbered ID when adding a new to-do item
@app.post("/todo", response_model=str)
async def add_todo_item(todo_item: TodoItemBase, current_user: Annotated[UserBase, Depends(get_current_user)]):
    try:
        todos = []
        async for todo in mongodb_handler.get_all_todo_data(current_user.username):
            todos.append(todo)
        # todos = await mongodb_handler.get_all_todo_data(current_user.username)
        max_id = max([todo.get('id', 0) for todo in todos]) if todos else 0
        item = todo_item.model_dump()
        item['id'] = max_id + 1  # Assign a new numeric ID
        item['created_by'] = current_user.username
        item['created_at'] = datetime.now(timezone.utc)
        item['updated_at'] = datetime.now(timezone.utc)
        result = await mongodb_handler.insert_todo_data(item)
        if result.inserted_id:
            return "Item added successfully"
        else:
            return "Unable to add todo item"
    except:
        logger.exception("Error in adding a todo item")


@app.get("/todos", response_model=List[TodoItem])  #response_model=List[Dict[Any, Any]]
async def get_todo_items(current_user: Annotated[UserBase, Depends(get_current_user)]):   #
    try:
        todos = []
        async for todo in mongodb_handler.get_all_todo_data(current_user.username):
            todos.append(todo)
        return todos
    except:
        logger.exception("Error getting all todo items")


@app.get("/todo/{id}", response_model=TodoItem)
async def get_todo_item(id: int, current_user: Annotated[UserBase, Depends(get_current_user)]):
    try:
        todo = await mongodb_handler.get_single_todo_data(id, current_user.username)  # Assuming you filter by user and ID
        if todo is None:
            raise HTTPException(status_code=404, detail="To-Do Item not found")
        return todo
    except:
        logger.exception("Error getting single todo item")


# Modify update function to use numeric ID
@app.put("/todo/{id}", response_model=TodoItem)
async def update_todo_item(id: int, todo_item: TodoItemBase, current_user: Annotated[UserBase, Depends(get_current_user)]):
    update_data = {k: v for k, v in todo_item.model_dump(exclude_unset=True).items() if v is not None}
    try:
        if update_data:
            update_data['updated_at'] = datetime.now(timezone.utc)
            result = await mongodb_handler.update_todo_data(id, update_data, current_user.username)

            if result.modified_count == 0:
                raise HTTPException(status_code=404, detail="To-Do Item not found")

        # Fetch the updated todo item after successful update
        updated_todo = await mongodb_handler.get_single_todo_data(id, current_user.username)
        if not updated_todo:
            raise HTTPException(status_code=404, detail="To-Do Item not found")

        return updated_todo

    except Exception as e:
        logger.exception("Failed to update the data")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Modify delete function to use numeric ID
@app.delete("/todo/{id}", response_model=dict)
async def delete_todo_item(id: int, current_user: Annotated[UserBase, Depends(get_current_user)]):
    try:
        result = await mongodb_handler.delete_todo_data(id, current_user.username)
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="To-Do Item not found")
        else:
            return "To-Do Item deleted successfully"
    except:
        logger.exception("Failed to delete the data")
