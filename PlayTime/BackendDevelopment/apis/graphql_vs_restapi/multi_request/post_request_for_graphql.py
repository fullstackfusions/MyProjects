import httpx
import asyncio

# Async function to send the GraphQL POST request
async def send_graphql_query():
    async with httpx.AsyncClient() as client:
        query = """
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
        """
        
        # Send the POST request to the GraphQL endpoint
        try:
            response = await client.post("http://127.0.0.1:8000/graphql", json={"query": query})
            # Print the response
            print("Response from GraphQL server:", response.json())
        except httpx.HTTPStatusError as exc:
            print(f"Error: {exc.response.status_code} {exc.response.text}")

if __name__ == "__main__":
    # Run the async request function
    asyncio.run(send_graphql_query())
