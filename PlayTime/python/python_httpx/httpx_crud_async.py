import httpx
import asyncio

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
async def create_item(data):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(base_url, headers=headers, json=data)
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
async def read_item(item_id):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{base_url}/{item_id}", headers=headers)
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
async def update_item(item_id, data):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(f"{base_url}/{item_id}", headers=headers, json=data)
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
async def delete_item(item_id):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"{base_url}/{item_id}", headers=headers)
            if response.status_code == 204:
                print("Item deleted successfully!")
            else:
                print(f"Delete failed with status code: {response.status_code}")
                print(response.text)
    except httpx.RequestError as e:
        print(f"An error occurred: {e}")

# Example usage:
async def main():
    item_data = {"name": "New Item", "description": "This is a new item"}
    await create_item(item_data)   # Create

    await read_item(1)             # Read item with ID 1

    await update_item(1, {"name": "Updated Item", "description": "Updated description"})  # Update

    await delete_item(1)           # Delete item with ID 1

# Run the async main function
asyncio.run(main())
