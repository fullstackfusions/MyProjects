"""
This file will demonstrate the simple requests practices
"""

import requests

# Base URL of the API (change this to the actual API endpoint)
api_url = "http://localhost:8000/items"

item_id = 1

# Data for the POST and PUT requests
item_data = {
    "name": "Sample Item",
    "description": "This is a sample item",
    "price": 19.99,
    "in_stock": True
}

def get_items():
    """ GET request to get existing items """
    response = requests.get(api_url, timeout=10)    # Increase this timeout if the data is larger and takes time
    if response.status_code == 201:
        print(f"Item created successfully: {response.json()}")
    else:
        print(f"Failed to create item: {response.status_code}, {response.text}")

def get_items(item_id):
    """ GET request to get an existing item """
    api_url = f"{api_url}/{item_id}"
    response = requests.get(api_url, timeout=10)    # Increase this timeout if the data is larger and takes time
    if response.status_code == 201:
        print(f"Item created successfully: {response.json()}")
    else:
        print(f"Failed to create item: {response.status_code}, {response.text}")


def create_item(item_data):
    """ POST request to create a new item """
    response = requests.post(api_url, json=item_data)
    if response.status_code == 201:
        print(f"Item created successfully: {response.json()}")
    else:
        print(f"Failed to create item: {response.status_code}, {response.text}")


def update_item(item_id, item_data):
    """ PUT request to update an existing item (assuming an item with ID 1) """
    update_url = f"{api_url}/{item_id}"
    response = requests.put(update_url, json=item_data)
    if response.status_code == 200:
        print(f"Item updated successfully: {response.json()}")
    else:
        print(f"Failed to update item: {response.status_code}, {response.text}")


def delete_item(item_id):
    """ DELETE request to remove an item (assuming an item with ID 1) """
    delete_url = f"{api_url}/{item_id}"
    response = requests.delete(delete_url)
    if response.status_code == 204:
        print(f"Item deleted successfully.")
    else:
        print(f"Failed to delete item: {response.status_code}, {response.text}")

