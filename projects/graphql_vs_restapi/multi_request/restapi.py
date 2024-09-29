"""

In this restapi approach you have to make two separate request to get the response of users and their posts

"""

from fastapi import FastAPI
import httpx
import logging

app = FastAPI()

# REST API to get user information
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # Simulate fetching user from external API
    user = {
        "id": user_id,
        "name": "John Doe",
        "email": "john@example.com"
    }
    return user

# REST API to get posts for a user
@app.get("/users/{user_id}/posts")
async def get_user_posts(user_id: int):
    # Simulate fetching posts from external API
    posts = [
        {"title": "Post 1", "content": "Content of post 1", "user_id": user_id},
        {"title": "Post 2", "content": "Content of post 2", "user_id": user_id}
    ]
    return posts

# REST API endpoint to fetch user and posts with multiple requests
@app.get("/user_with_posts_rest/{user_id}")
async def get_user_with_posts_rest(user_id: int):
    print(user_id)
    print("hello")

    try:
        async with httpx.AsyncClient() as client:
            # Fetch user information
            user_response = await client.get(f"http://127.0.0.1:8000/users/{user_id}")
            user = user_response.json()

            # Fetch user's posts
            posts_response = await client.get(f"http://127.0.0.1:8000/users/{user_id}/posts")
            posts = posts_response.json()

        print("hello2")
        return {"user": user, "posts": posts}
    except Exception as e:
        logging.exception("Error fetching data")
        return {"error": "Failed to fetch data"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
