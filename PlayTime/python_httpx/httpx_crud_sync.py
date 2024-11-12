import httpx
import json

# API base URL
base_url = "https://example.com/api/resource"

# Headers for the requests
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# -----------------------------
# Create operation (POST request)
# -----------------------------
def create_item(data):
    try:
        with httpx.Client() as client:
            response = client.post(base_url, headers=headers, json=data)
            if response.status_code == 201:
                print("Item created successfully!")
                print(response.json())
            else:
                print(f"Create failed with status code: {response.status_code}")
                print(response.text)
    except httpx.RequestError as e:
        print(f"An error occurred: {e}")

# -----------------------------
# Read operation (GET request)
# -----------------------------
def read_item(item_id):
    try:
        with httpx.Client() as client:
            response = client.get(f"{base_url}/{item_id}", headers=headers)
            if response.status_code == 200:
                print("Item fetched successfully!")
                print(response.json())
            else:
                print(f"Read failed with status code: {response.status_code}")
                print(response.text)
    except httpx.RequestError as e:
        print(f"An error occurred: {e}")

# -----------------------------
# Update operation (PUT request)
# -----------------------------
def update_item(item_id, data):
    try:
        with httpx.Client() as client:
            response = client.put(f"{base_url}/{item_id}", headers=headers, json=data)
            if response.status_code == 200:
                print("Item updated successfully!")
                print(response.json())
            else:
                print(f"Update failed with status code: {response.status_code}")
                print(response.text)
    except httpx.RequestError as e:
        print(f"An error occurred: {e}")

# -----------------------------
# Delete operation (DELETE request)
# -----------------------------
def delete_item(item_id):
    try:
        with httpx.Client() as client:
            response = client.delete(f"{base_url}/{item_id}", headers=headers)
            if response.status_code == 204:
                print("Item deleted successfully!")
            else:
                print(f"Delete failed with status code: {response.status_code}")
                print(response.text)
    except httpx.RequestError as e:
        print(f"An error occurred: {e}")

# Example usage:
item_data = {"name": "New Item", "description": "This is a new item"}
create_item(item_data)   # Create

read_item(1)             # Read item with ID 1

update_item(1, {"name": "Updated Item", "description": "Updated description"})  # Update

delete_item(1)           # Delete item with ID 1
