"""

In this script we are running api calls in parallel, this api calls can be used for pagination in parallel.

Saving results in s3 bucket

"""

import json
import boto3
import requests
import time
from multiprocessing import Pool
import logging

# Initialize boto3 S3 client
s3 = boto3.client('s3')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_json_to_s3(data, key):
    """Helper function to save JSON data to a file in S3."""
    s3_bucket_name = 'your-s3-bucket-name'
    json_data = json.dumps(data, indent=4)
    s3.put_object(Body=json_data, Bucket=s3_bucket_name, Key=key)

def fetch_and_store_paginated_data(api_info, retries=3, retry_delay=5):
    """Fetch and store paginated API data into S3 with retry logic."""
    base_url, pagination_type, skip, limit, directory_name = api_info
    data = None
    attempt = 0
    
    while attempt < retries:
        try:
            # Fetch data based on the pagination type
            if pagination_type == 'skip':
                response = requests.get(f"{base_url}?limit={limit}&skip={skip}")
                response.raise_for_status()
                data = response.json()
            elif pagination_type == 'count':
                response = requests.get(f"{base_url}?count={limit}&offset={skip}")
                response.raise_for_status()
                data = response.json()
            elif pagination_type == 'page':
                response = requests.get(f"{base_url}?limit={limit}&page={skip}")
                response.raise_for_status()
                data = response.json()
            
            # If data is successfully fetched, store it in S3
            if data:
                file_name = ""
                if pagination_type == 'skip':
                    file_name = f"{directory_name}/paginated_response_{skip}_{skip+limit}.json"
                elif pagination_type == 'count':
                    file_name = f"{directory_name}/paginated_response_{skip}_{skip+limit}.json"
                elif pagination_type == 'page':
                    file_name = f"{directory_name}/paginated_response_page_{skip}.json"
                
                # Save to S3
                save_json_to_s3(data, file_name)
                logger.info(f"Saved {file_name} to S3")
                return  # Exit the function after successful save

        except:
            logger.exception(f"Error fetching data from {base_url}")
            attempt += 1
            if attempt < retries:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logger.error(f"Max retries reached. Logging error.")
                # Optionally, log more details or send notifications
                break  # Exit loop after max retries

def process_api_in_parallel(base_url, pagination_type, skip, limit, directory_name, num_workers=8):
    """Process API pagination using multiprocessing.Pool for parallelism."""
    
    # Build a list of arguments to pass to fetch_and_store_paginated_data
    tasks = []
    
    tasks.append((base_url, pagination_type, skip, limit, directory_name))

    # Use multiprocessing Pool to run tasks in parallel
    with Pool(processes=num_workers) as pool:
        pool.map(fetch_and_store_paginated_data, tasks)

def run_all_apis_in_parallel():
    """Main function to run all APIs in parallel with multiprocessing."""
    base_url_api1 = "https://example.com/api1"
    base_url_api2 = "https://example.com/api2"
    base_url_api3 = "https://example.com/api3"
    
    # API 1: Skip/Limit Pagination
    process_api_in_parallel(
        base_url=base_url_api1,
        pagination_type="skip",
        skip=0,
        limit=100,
        directory_name="source1"
    )

    # API 2: Count/Offset Pagination
    process_api_in_parallel(
        base_url=base_url_api2,
        pagination_type="count",
        skip=0,
        limit=10000,
        directory_name="source2"
    )

    # API 3: Page/Limit Pagination
    process_api_in_parallel(
        base_url=base_url_api3,
        pagination_type="page",
        skip=0,
        limit=10000,
        directory_name="source3"
    )

# Run the script
if __name__ == '__main__':
    run_all_apis_in_parallel()