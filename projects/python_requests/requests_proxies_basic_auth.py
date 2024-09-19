"""
This file will demonstrate the simple requests practices

includes requests, basic authentications, proxies
"""

import requests
from requests.auth import HTTPBasicAuth

# API endpoint
url = "https://example.com/api/endpoint?param=value"

# Authentication details
username = "your_username"
password = "your_password"

# Proxy details (if required)
proxies = {
    "http": "http://username:password@your_proxy:proxy_port",
    "https": "http://username:password@your_proxy:proxy_port",
    "all": "http://username:password@your_proxy:proxy_port",
    "ftp": "http://username:password@your_proxy:proxy_port",
    "no": "127.0.0.*,172.*,10.*,192.168.*,localhost"
}

try:
    # Make the GET request with basic auth and proxy settings
    response = requests.get(
        url,
        auth=HTTPBasicAuth(username, password),
        proxies=proxies,
        timeout=10  # Set timeout to avoid long hangs
    )
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful!")
        print(response.json())  # Assuming the response is in JSON format
    else:
        print(f"Failed with status code: {response.status_code}")
        print(response.text)  # To see the error message from the server

except requests.exceptions.ProxyError as proxy_err:
    print("Proxy error occurred:", proxy_err)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
