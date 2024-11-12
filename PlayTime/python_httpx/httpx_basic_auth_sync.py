import httpx

# API endpoint
url = "https://example.com/api/resource"

# Credentials for Basic Auth
username = "your_username"
password = "your_password"

# GET request with Basic Auth
def get_with_basic_auth():
    with httpx.Client(auth=(username, password)) as client:
        response = client.get(url)
        if response.status_code == 200:
            print("GET request successful with Basic Auth!")
            print(response.json())
        else:
            print(f"GET failed with status code: {response.status_code}")

# POST request with Basic Auth
def post_with_basic_auth(data):
    with httpx.Client(auth=(username, password)) as client:
        response = client.post(url, json=data)
        if response.status_code == 201:
            print("POST request successful with Basic Auth!")
            print(response.json())
        else:
            print(f"POST failed with status code: {response.status_code}")

# Example usage
get_with_basic_auth()
post_with_basic_auth({"key": "value"})
