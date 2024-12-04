"""

In this example, we are using Hasura tool's graphql api. Info on Hasura: https://hasura.io/

Hasura is very useful tool to query either in Rest or GraphQL architecture to Datawarehouse. Here we have used SQL Server as Datawarehouse.

"""

import requests
import json
from datetime import datetime, timedelta
import base64

def get_paginated_response(limit, offset):
    graphql_url = "https://<hasura_server_instance_url>/v1/graphql"

    query = """
        query MyQuery($limit:Int!, $offset:Int!) {
            your_table_name(limit: $limit, offset: $offset) {
                id
                ip
                Name
                other_columns
            }
        }
    """

    # Username and password for Basic Auth
    username = "your_username"
    password = "your_password"

    # Encode the username and password for Basic Authentication
    auth_string = f"{username}:{password}"
    encoded_auth_string = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

    headers = {
        "content-type": "application/json",
        "x-hasura-admin-secret": "admin",
        "Authorization": f"Basic {encoded_auth_string}"
    }

    variables = {
        "limit": limit,
        "offset": offset
    }

    response = requests.post(graphql_url, headers=headers, json={"query": query, "variables": variables}, verify=False)

    if response.status_code == 200:
        return response
    else:
        print(f"Failed to fetch data. HTTP status code: {response.status_code}")
        print(f"Error: {response.text}")

def loop():
    limit = 100
    offset = 0

    while True:
        response = get_paginated_response(limit, offset)
        data = response.json()
        data_list = data["data"]["your_table_name"]
        
        if not data_list:
            break

        offset += limit

        # The following logic is to store data in file, you can also use s3 bucket connection using boto3 to store data into s3 bucket
        file_name = f"offset_{offset}_hasura_response.json"
        with open(file_name, "a") as f:
            for item in data_list:
                # Convert each item to JSON format and append to the file
                f.write(json.dumps(item, indent=4) + "\n")

if __name__ == "__main__":
    loop()