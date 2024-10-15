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

def save_json_to_s3(data, bucket_name, key):
    """Helper function to save JSON data to a file in S3."""
    json_data = json.dumps(data, indent=4)
    s3.put_object(Body=json_data, Bucket=bucket_name, Key=key)

def fetch_and_store_paginated_data(api_info, retries=3, retry_delay=5):
    """Fetch and store paginated API data into S3 with retry logic."""
    base_url, pagination_type, bucket_name, directory_name, start, limit, max_records = api_info
    data = None
    attempt = 0
    
    while attempt < retries:
        try:
            # Fetch data based on the pagination type
            if pagination_type == 'skip':
                response = requests.get(f"{base_url}?limit={limit}&skip={start}")
                response.raise_for_status()
                data = response.json()
            elif pagination_type == 'count':
                response = requests.get(f"{base_url}?count={limit}&offset={start}")
                response.raise_for_status()
                data = response.json()
            elif pagination_type == 'page':
                response = requests.get(f"{base_url}?limit={limit}&page={start}")
                response.raise_for_status()
                data = response.json()
            
            # If data is successfully fetched, store it in S3
            if data:
                file_name = ""
                if pagination_type == 'skip':
                    file_name = f"{directory_name}/paginated_response_{start}_{start+limit}.json"
                elif pagination_type == 'count':
                    file_name = f"{directory_name}/paginated_response_{start}_{start+limit}.json"
                elif pagination_type == 'page':
                    file_name = f"{directory_name}/paginated_response_page_{start}.json"
                
                # Save to S3
                save_json_to_s3(data, bucket_name, file_name)
                logger.info(f"Saved {file_name} to S3")
                return  # Exit the function after successful save

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from {base_url} for {pagination_type} {start}: {str(e)}")
            attempt += 1
            if attempt < retries:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logger.error(f"Max retries reached for {pagination_type} {start}. Logging error.")
                # Optionally, log more details or send notifications
                break  # Exit loop after max retries

def process_api_in_parallel(base_url, pagination_type, bucket_name, directory_name, limit, max_records, num_workers=4):
    """Process API pagination using multiprocessing.Pool for parallelism."""
    
    # Build a list of arguments to pass to fetch_and_store_paginated_data
    tasks = []
    
    if pagination_type == 'skip':
        for skip in range(0, max_records, limit):
            tasks.append((base_url, 'skip', bucket_name, directory_name, skip, limit, max_records))
    
    elif pagination_type == 'count':
        for offset in range(0, max_records, limit):
            tasks.append((base_url, 'count', bucket_name, directory_name, offset, limit, max_records))
    
    elif pagination_type == 'page':
        pages = (max_records // limit) + 1
        for page in range(1, pages + 1):
            tasks.append((base_url, 'page', bucket_name, directory_name, page, limit, max_records))

    # Use multiprocessing Pool to run tasks in parallel
    with Pool(processes=num_workers) as pool:
        pool.map(fetch_and_store_paginated_data, tasks)

def run_all_apis_in_parallel(bucket_name):
    """Main function to run all APIs in parallel with multiprocessing."""
    base_url_api1 = "https://example.com/api1"
    base_url_api2 = "https://example.com/api2"
    base_url_api3 = "https://example.com/api3"
    
    # API 1: Skip/Limit Pagination
    process_api_in_parallel(
        base_url=base_url_api1,
        pagination_type='skip',
        bucket_name=bucket_name,
        directory_name='api1',
        limit=100,
        max_records=350000,
        num_workers=8
    )

    # API 2: Count/Offset Pagination
    process_api_in_parallel(
        base_url=base_url_api2,
        pagination_type='count',
        bucket_name=bucket_name,
        directory_name='api2',
        limit=10000,
        max_records=15000,
        num_workers=8
    )

    # API 3: Page/Limit Pagination
    process_api_in_parallel(
        base_url=base_url_api3,
        pagination_type='page',
        bucket_name=bucket_name,
        directory_name='api3',
        limit=100,
        max_records=700000,
        num_workers=8
    )

# Run the script
if __name__ == '__main__':
    s3_bucket_name = 'your-s3-bucket-name'
    run_all_apis_in_parallel(s3_bucket_name)