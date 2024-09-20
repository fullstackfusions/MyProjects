"""
In the asynchronous version, we use httpx.AsyncClient() along with await to handle non-blocking requests, allowing other tasks to be run concurrently if needed.
"""

import httpx
import asyncio

async def fetch_all_users():
    url = "https://api.github.com/users"
    all_users = []
    page = 1

    async with httpx.AsyncClient() as client:
        while True:
            params = {'per_page': 50, 'page': page}
            response = await client.get(url, params=params)
            data = response.json()

            if not data:  # Break if there's no more data
                break

            all_users.extend(data)
            page += 1

    print(f"Total users fetched: {len(all_users)}")

# Run the async function
asyncio.run(fetch_all_users())
