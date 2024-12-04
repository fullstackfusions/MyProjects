import httpx
import asyncio

# API endpoint
url = "https://example.com/api/resource"

# Token for Authentication
token = "your_api_token"

# GET request with Token Auth (Async)
async def get_with_token_auth():
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            print("GET request successful with Token Auth!")
            print(response.json())
        else:
            print(f"GET failed with status code: {response.status_code}")

# POST request with Token Auth (Async)
async def post_with_token_auth(data):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print("POST request successful with Token Auth!")
            print(response.json())
        else:
            print(f"POST failed with status code: {response.status_code}")

# Example usage
async def main():
    await get_with_token_auth()
    await post_with_token_auth({"key": "value"})

asyncio.run(main())
