import httpx
import asyncio

# API endpoint
url = "https://example.com/api/resource"

# Credentials for Basic Auth
username = "your_username"
password = "your_password"

# GET request with Basic Auth (Async)
async def get_with_basic_auth():
    async with httpx.AsyncClient(auth=(username, password)) as client:
        response = await client.get(url)
        if response.status_code == 200:
            print("GET request successful with Basic Auth!")
            print(response.json())
        else:
            print(f"GET failed with status code: {response.status_code}")

# POST request with Basic Auth (Async)
async def post_with_basic_auth(data):
    async with httpx.AsyncClient(auth=(username, password)) as client:
        response = await client.post(url, json=data)
        if response.status_code == 201:
            print("POST request successful with Basic Auth!")
            print(response.json())
        else:
            print(f"POST failed with status code: {response.status_code}")

# Example usage
async def main():
    await get_with_basic_auth()
    await post_with_basic_auth({"key": "value"})

asyncio.run(main())
