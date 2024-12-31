"""

In this graphql approach you have to make only one separate request to get the response of users and their posts, using post request mentioned in "post_request_for_graphql.py"

"""

from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# GraphQL API endpoint in FastAPI
@app.post("/graphql")
async def graphql_endpoint(request: Request):
    body = await request.json()  # Parse JSON body of the request
    query = body.get("query", "")

    # Simplify the query to remove extra spaces and line breaks
    simplified_query = query.replace("\n", "").replace(" ", "").replace("\t", "")
    
    # Expected query
    expected_query = """
    {
      user(id: 1) {
        id
        name
        email
        posts {
          title
          content
        }
      }
    }
    """.replace("\n", "").replace(" ", "").replace("\t", "")
    
    if simplified_query == expected_query:
        # Simulated response data
        data = {
            "data": {
                "user": {
                    "id": 1,
                    "name": "John Doe",
                    "email": "john@example.com",
                    "posts": [
                        {"title": "Post 1", "content": "Content of post 1"},
                        {"title": "Post 2", "content": "Content of post 2"}
                    ]
                }
            }
        }
        return data
    else:
        return {"error": "Query not recognized"}

if __name__ == "__main__":
    # Run the FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=8000)
