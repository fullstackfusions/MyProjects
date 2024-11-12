"""
This file demonstrate how to pass token in api request

"""

import requests
import logging
import json

def get_token():
    username = "username"
    password = "password"

    body = {
        "username": username,
        "password": password
    }

    token_url = "https://example.com/api/toke_endpoint"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        response = requests.get(token_url, headers=headers, data=json.dumps(body), verify=False)    # Usually keep verify True if you have security certificates setup

        if response.status_code == 200:
            json_result = response.json()
            return json_result
        else:
            print("Get token failed! - " + str(response.text))
    except:
        logging.exeption("Error in getting token")

def get_response():
    api_endpoint = "https://example.com/api/api_endpoint"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    token = get_token()
    headers["Token"] = token["token"]

    params = {
        "some_required_params": "params_values"
    }

    # Proxy details (if required)
    proxies = {
        "http": "http://username:password@your_proxy:proxy_port",
        "https": "http://username:password@your_proxy:proxy_port",
        "all": "http://username:password@your_proxy:proxy_port",
        "ftp": "http://username:password@your_proxy:proxy_port",
        "no": "127.0.0.*,172.*,10.*,192.168.*,localhost"
    }
    
    try:
        # Make the GET request with token and proxy settings
        response = requests.get(
            api_endpoint,
            params=params,
            headers=headers,
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
        # or you can also use following best practice
        logging.exception("Proxy error occurred:")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        # or you can also use following best practice
        logging.exception("An error occurred:")
