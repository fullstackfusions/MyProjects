import httpx

# API endpoint
url = "https://example.com/api/resource"

# Token for Authentication
token = "your_api_token"

# GET request with Token Auth
def get_with_token_auth():
    headers = {"Authorization": f"Bearer {token}"}
    with httpx.Client() as client:
        response = client.get(url, headers=headers)
        if response.status_code == 200:
            print("GET request successful with Token Auth!")
            print(response.json())
        else:
            print(f"GET failed with status code: {response.status_code}")

# POST request with Token Auth
def post_with_token_auth(data):
    headers = {"Authorization": f"Bearer {token}"}
    with httpx.Client() as client:
        response = client.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print("POST request successful with Token Auth!")
            print(response.json())
        else:
            print(f"POST failed with status code: {response.status_code}")

# Example usage
get_with_token_auth()
post_with_token_auth({"key": "value"})
