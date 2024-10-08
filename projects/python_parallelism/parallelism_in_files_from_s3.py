import json
import boto3
from multiprocessing import Pool

# Initialize the boto3 S3 client
s3 = boto3.client('s3')

def load_json_s3(bucket_name, key):
    """Helper function to load JSON data from a file stored in S3."""
    obj = s3.get_object(Bucket=bucket_name, Key=key)
    data = obj['Body'].read().decode('utf-8')
    return json.loads(data)

def save_json_s3(data, bucket_name, key):
    """Helper function to save JSON data to a file in S3."""
    json_data = json.dumps(data, indent=4)
    s3.put_object(Body=json_data, Bucket=bucket_name, Key=key)

def build_lookup_table_hasura(files, bucket_name, key):
    """Build a lookup table for fast matching from hasura_filtered, extracting only DeviceName and NeighborIPDotted."""
    lookup = {}
    for file in files:
        data = load_json_s3(bucket_name, file)
        for obj in data:
            device_name = obj.get(key)
            neighbor_ip = obj.get("NeighborIPDotted")
            if device_name and neighbor_ip:
                if device_name in lookup:
                    lookup[device_name].append(neighbor_ip)
                else:
                    lookup[device_name] = [neighbor_ip]
    return lookup

def build_lookup_table_neighbors(files, bucket_name, key):
    """Build a lookup table for fast matching from netbrain_neighbors_L2, extracting only hostname and neighbors."""
    lookup = {}
    for file in files:
        data = load_json_s3(bucket_name, file)
        for obj in data:
            hostname = obj.get(key)
            neighbors = obj.get("neighbors")
            if hostname and neighbors:
                if hostname in lookup:
                    lookup[hostname].extend(neighbors)
                else:
                    lookup[hostname] = neighbors
    return lookup

def process_part3_file(part3_file, part1_lookup, part2_lookup, bucket_name):
    """Process a single part3 file by matching with part1 and part2 lookup tables."""
    part3_data = load_json_s3(bucket_name, part3_file)
    updated_part3_data = []

    # Iterate over the data in part3 and check for matches in part1 and part2 lookups
    for obj3 in part3_data:
        switch_name = obj3.get("switchName")
        combined_obj = obj3.copy()

        # Lookup part1 data (DeviceName)
        if switch_name in part1_lookup:
            combined_obj.update({
                "NeighborIPDotted": part1_lookup[switch_name]
            })

        # Lookup part2 data (hostname)
        if switch_name in part2_lookup:
            combined_obj.update({
                "neighbors": part2_lookup[switch_name]
            })

        updated_part3_data.append(combined_obj)

    return updated_part3_data

def process_files_in_parallel(bucket_name, part1_prefix, part2_prefix, part3_prefix, output_prefix, num_workers=4):
    """Main function to process files from part1, part2, part3 directories in parallel on S3."""

    # List all files from S3 using the provided prefixes
    part1_files = [obj['Key'] for obj in s3.list_objects_v2(Bucket=bucket_name, Prefix=part1_prefix)['Contents']]
    part2_files = [obj['Key'] for obj in s3.list_objects_v2(Bucket=bucket_name, Prefix=part2_prefix)['Contents']]
    part3_files = [obj['Key'] for obj in s3.list_objects_v2(Bucket=bucket_name, Prefix=part3_prefix)['Contents']]

    # Preload part1 and part2 data into lookup tables
    print("Building lookup tables...")
    part1_lookup = build_lookup_table_hasura(part1_files, bucket_name, "DeviceName")
    part2_lookup = build_lookup_table_neighbors(part2_files, bucket_name, "hostname")

    print("Starting parallel processing...")
    # Use Pool to parallelize processing of part3 files
    with Pool(processes=num_workers) as pool:
        futures = []
        for part3_file in part3_files:
            # Submit the file processing task to the pool
            futures.append(
                pool.apply_async(process_part3_file, (part3_file, part1_lookup, part2_lookup, bucket_name))
            )

        # Collect the results and write to S3
        for i, future in enumerate(futures):
            updated_part3_data = future.get()  # Get the result of the async task
            output_file_path = f"{output_prefix}{part3_files[i].split('/')[-1]}"
            save_json_s3(updated_part3_data, bucket_name, output_file_path)


# Use this block to prevent multiprocessing issues on some platforms
if __name__ == '__main__':
    bucket_name = 'your-s3-bucket-name'
    part1_prefix = 'hasura_filtered/'
    part2_prefix = 'netbrain/netbrain_neighbors_L2/'
    part3_prefix = 'netbrain/new_individual/'
    output_prefix = 'updated_output/'

    # Process the files in parallel
    process_files_in_parallel(bucket_name, part1_prefix, part2_prefix, part3_prefix, output_prefix, num_workers=4)
