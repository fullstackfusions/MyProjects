## Example: Weather Data Service

Creating a service using Python and providing an API key on signup involves several steps, including user authentication, generating and managing API keys, and providing a functional service that users can access via these keys. Below is an example of how you might implement such a service.

#### Step-by-Step Implementation

1. **Set Up Your Environment**:
   Install necessary packages:

   ```bash
   pip install fastapi uvicorn pydantic sqlalchemy passlib bcrypt
   ```

2. **Database Setup**:
   Use SQLite for simplicity. Set up SQLAlchemy for ORM.

3. **Create the Project Structure**:

   ```
   weather_service/
   ├── main.py
   ├── models.py
   ├── schemas.py
   ├── database.py
   ├── auth.py
   └── weather.py
   ```

4. **`database.py`**:

   ```python
   from sqlalchemy import create_engine, Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

   engine = create_engine(SQLALCHEMY_DATABASE_URL)
   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   Base = declarative_base()

   def get_db():
       db = SessionLocal()
       try:
           yield db
       finally:
           db.close()
   ```

5. **`models.py`**:

   ```python
   from sqlalchemy import Column, Integer, String
   from .database import Base

   class User(Base):
       __tablename__ = "users"
       id = Column(Integer, primary_key=True, index=True)
       email = Column(String, unique=True, index=True)
       hashed_password = Column(String)
       api_key = Column(String, unique=True, index=True)
   ```

6. **`schemas.py`**:

   ```python
   from pydantic import BaseModel

   class UserCreate(BaseModel):
       email: str
       password: str

   class User(BaseModel):
       email: str
       api_key: str

       class Config:
           orm_mode = True
   ```

7. **`auth.py`**:

   ```python
   from passlib.context import CryptContext
   import secrets

   pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

   def verify_password(plain_password, hashed_password):
       return pwd_context.verify(plain_password, hashed_password)

   def get_password_hash(password):
       return pwd_context.hash(password)

   def generate_api_key():
       return secrets.token_hex(32)
   ```

8. **`main.py`**:

   ```python
   from fastapi import FastAPI, Depends, HTTPException, status
   from sqlalchemy.orm import Session
   from . import models, schemas, auth, database
   from .database import engine, get_db

   models.Base.metadata.create_all(bind=engine)

   app = FastAPI()

   @app.post("/signup", response_model=schemas.User)
   def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
       db_user = db.query(models.User).filter(models.User.email == user.email).first()
       if db_user:
           raise HTTPException(status_code=400, detail="Email already registered")

       hashed_password = auth.get_password_hash(user.password)
       api_key = auth.generate_api_key()
       new_user = models.User(email=user.email, hashed_password=hashed_password, api_key=api_key)

       db.add(new_user)
       db.commit()
       db.refresh(new_user)
       return new_user

   @app.get("/weather")
   def get_weather_data(api_key: str, db: Session = Depends(get_db)):
       user = db.query(models.User).filter(models.User.api_key == api_key).first()
       if not user:
           raise HTTPException(status_code=400, detail="Invalid API Key")

       # Example weather data
       weather_data = {
           "location": "San Francisco",
           "temperature": "15°C",
           "condition": "Cloudy"
       }
       return weather_data
   ```

9. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

#### Explanation

1. **Database and Models**:

   - `database.py` sets up the SQLite database and session management.
   - `models.py` defines the `User` model with fields for `email`, `hashed_password`, and `api_key`.

2. **Schemas**:

   - `schemas.py` defines Pydantic models for creating users and returning user information.

3. **Authentication**:

   - `auth.py` includes functions for password hashing, verifying, and API key generation.

4. **API Endpoints**:
   - `main.py` includes endpoints for user signup (`/signup`) and accessing weather data (`/weather`).
   - On signup, a new user is created with a hashed password and a unique API key.
   - The `/weather` endpoint checks for a valid API key before returning weather data.

### Usage

1. **Sign Up**:
   Make a POST request to `/signup` with email and password.

   ```json
   {
     "email": "user@example.com",
     "password": "password123"
   }
   ```

   The response will include the API key.

2. **Access Weather Data**:
   Make a GET request to `/weather` with the API key.
   ```
   GET /weather?api_key=<your_api_key>
   ```
   The response will include weather data.

This example demonstrates how to create a simple service with user authentication, API key generation, and secure access to a protected endpoint.
