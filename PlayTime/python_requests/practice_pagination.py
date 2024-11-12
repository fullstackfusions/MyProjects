import requests

url = "https://api.github.com/users"
all_users = []
page = 1

while True:
    params = {'per_page': 50, 'page': page}
    response = requests.get(url, params=params)
    data = response.json()
    
    if not data:  # Break if there's no more data
        break
    
    all_users.extend(data)
    page += 1

print(f"Total users fetched: {len(all_users)}")
