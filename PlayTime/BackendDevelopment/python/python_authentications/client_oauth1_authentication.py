"""

Use Case: An older version of OAuth, mainly used by services like Twitter that haven't fully migrated to OAuth 2.0.

Common in: Legacy systems, some social media platforms like Twitter.

Security: Secure but complex, and largely replaced by OAuth 2.0 in modern applications.

"""

import requests
from requests_oauthlib import OAuth1

# Define the API endpoint
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# OAuth 1.0 credentials
client_key = "your_client_key"
client_secret = "your_client_secret"
resource_owner_key = "your_access_token"
resource_owner_secret = "your_access_token_secret"

# Setup OAuth1 authentication
auth = OAuth1(client_key, client_secret, resource_owner_key, resource_owner_secret)

# Send a GET request with OAuth 1.0 authentication
response = requests.get(url, auth=auth)

# Print the response status code and content
print(response.status_code)
print(response.json())
