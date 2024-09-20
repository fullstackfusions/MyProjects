import httpx
import logging
import json
import asyncio

async def get_token():
    username = "username"
    password = "password"

    body = {
        "username": username,
        "password": password
    }

    token_url = "https://example.com/api/token_endpoint"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        async with httpx.AsyncClient(verify=False) as client:  # Set verify=False if SSL certificate is not required
            response = await client.post(token_url, headers=headers, json=body)
            if response.status_code == 200:
                json_result = response.json()
                return json_result
            else:
                print(f"Get token failed! - {response.text}")
    except Exception as e:
        logging.exception("Error in getting token")
        return None

async def get_response():
    api_endpoint = "https://example.com/api/api_endpoint"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    token = await get_token()
    if not token:
        print("Failed to get token")
        return

    headers["Token"] = token.get("token")

    params = {
        "some_required_params": "params_values"
    }

    # Proxy details (if required)
    proxies = {
        "http://": "http://username:password@your_proxy:proxy_port",
        "https://": "http://username:password@your_proxy:proxy_port",
    }

    try:
        async with httpx.AsyncClient(proxies=proxies, timeout=10) as client:
            response = await client.get(api_endpoint, params=params, headers=headers)
            
            if response.status_code == 200:
                print("Request successful!")
                print(response.json())  # Assuming the response is in JSON format
            else:
                print(f"Failed with status code: {response.status_code}")
                print(response.text)
    except httpx.ProxyError as proxy_err:
        logging.exception("Proxy error occurred:", proxy_err)
    except httpx.RequestError as e:
        logging.exception(f"An error occurred: {e}")

# Run the async function
asyncio.run(get_response())
