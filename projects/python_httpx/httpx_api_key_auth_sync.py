import httpx

# API endpoint
url = "https://example.com/api/resource"

# API Key for Authentication
api_key = "your_api_key"

# GET request with API Key Auth
def get_with_api_key_auth():
    headers = {"X-API-Key": api_key}
    with httpx.Client() as client:
        response = client.get(url, headers=headers)
        if response.status_code == 200:
            print("GET request successful with API Key Auth!")
            print(response.json())
        else:
            print(f"GET failed with status code: {response.status_code}")

# POST request with API Key Auth
def post_with_api_key_auth(data):
    headers = {"X-API-Key": api_key}
    with httpx.Client() as client:
        response = client.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print("POST request successful with API Key Auth!")
            print(response.json())
        else:
            print(f"POST failed with status code: {response.status_code}")

# Example usage
get_with_api_key_auth()
post_with_api_key_auth({"key": "value"})
