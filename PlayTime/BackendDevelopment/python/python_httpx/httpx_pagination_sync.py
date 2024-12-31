"""
In the synchronous version, we use httpx.Client() similar to requests to handle the HTTP requests.
"""

import httpx

url = "https://api.github.com/users"
all_users = []
page = 1

with httpx.Client() as client:
    while True:
        params = {'per_page': 50, 'page': page}
        response = client.get(url, params=params)
        data = response.json()

        if not data:  # Break if there's no more data
            break

        all_users.extend(data)
        page += 1

print(f"Total users fetched: {len(all_users)}")
