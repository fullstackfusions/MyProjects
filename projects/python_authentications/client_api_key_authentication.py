"""

Use Case: Common for simple API access where a full-fledged OAuth or token system isn't necessary.

Common in: Public APIs, internal services, SaaS applications, and when there's minimal user interaction.

Security: API keys are generally less secure than token-based authentication, as they can be easily exposed if not handled carefully. Should always be used over HTTPS and rotated regularly.

"""


import requests

# Define the API endpoint
url = "https://api.example.com/register"
username = "username"

response = requests.post(url, params={"username": username})
response = response.json()
api_key = response["api_key"]


# Define the API endpoint to get data and pass api key in it.
url = "https://api.example.com/data"

# Approach 1: provide api key in params
# Send a GET request with the API key in the query parameters
response = requests.get(url, params={"api_key": api_key})


# Approach 2: provide api key in headers
# Send a GET request with the API key in the headers
headers = {
    "Authorization": f"ApiKey {api_key}"
}

response = requests.get(url, headers=headers)

# Print the response status code and content
print(response.status_code)
print(response.json())
