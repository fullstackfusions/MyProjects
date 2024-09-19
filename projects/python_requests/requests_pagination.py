"""
This script demonstrate the pagination in requests

"""

import requests

# Approach: 1

api_url = "https://api.example.com/data"  # Replace with your API URL
all_data = []
page = 1  # Starting page number

while True:
    # Replace 'page' with the appropriate parameter for the API
    params = {
        'page': page,
        'limit': 50  # Adjust the limit if the API allows for larger responses
    }
    
    response = requests.get(api_url, params=params)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        break
    
    data = response.json()
    
    if not data:  # Stop if there's no more data
        break
    
    all_data.extend(data)
    
    # Increment page number for next request
    page += 1

print(f"Retrieved {len(all_data)} records in total.")


# Approach: 2
# Sometimes pagination handling is different for different apis
# For example, it sometimes require to skip the initial fetch as following


api_url = "https://api.example.com/data"  # Replace with your API URL
all_data = []
skip = 0

while True:
    # Replace 'page' with the appropriate parameter for the API
    params = {
        'skip': skip,
    }
    
    response = requests.get(api_url, params=params)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        break
    
    data = response.json()
    count = len(data) # this is specific count that we want to skip from last fetch
    skip = skip + count # we are adding the current count's to last count

    
    if not data:  # Stop if there's no more data
        break
    
    all_data.extend(data)
    

print(f"Retrieved {len(all_data)} records in total.")
