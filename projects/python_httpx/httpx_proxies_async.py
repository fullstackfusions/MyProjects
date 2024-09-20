"""
This file will demonstrate the simple requests practices

includes requests, basic authentications, proxies

Asynchronous version: Uses httpx.AsyncClient() along with await for non-blocking HTTP requests.
"""


import httpx
import asyncio

# API endpoint
url = "https://example.com/api/endpoint?param=value"

# Authentication details
username = "your_username"
password = "your_password"

# Proxy details (if required)
proxies = {
    "http://": "http://username:password@your_proxy:proxy_port",
    "https://": "http://username:password@your_proxy:proxy_port",
}

async def fetch_data():
    try:
        async with httpx.AsyncClient(proxies=proxies, timeout=10) as client:
            # Make the GET request with basic auth and proxy settings
            response = await client.get(url, auth=(username, password))
            
            # Check if the request was successful
            if response.status_code == 200:
                print("Request successful!")
                print(response.json())  # Assuming the response is in JSON format
            else:
                print(f"Failed with status code: {response.status_code}")
                print(response.text)  # To see the error message from the server

    except httpx.ProxyError as proxy_err:
        print("Proxy error occurred:", proxy_err)

    except httpx.RequestError as e:
        print(f"An error occurred: {e}")

# Run the async function
asyncio.run(fetch_data())
