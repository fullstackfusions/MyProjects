import tracemalloc
import boto3
import json

def read_json_files_from_s3(bucket_name, file_keys):
    """Simulate reading JSON files from S3."""
    s3 = boto3.client('s3')
    all_data = []
    for key in file_keys:
        response = s3.get_object(Bucket=bucket_name, Key=key)
        data = json.loads(response['Body'].read().decode('utf-8'))
        all_data.extend(data)  # Assume data is a list of lists
    return all_data

def process_data(data):
    """Simulate processing data: delisting, mapping, and cleaning."""
    flattened_data = [item for sublist in data for item in sublist]
    mapped_data = [{"id": i, "value": value} for i, value in enumerate(flattened_data)]
    cleaned_data = [item for item in mapped_data if item["value"] is not None]
    return cleaned_data

def upload_to_s3(bucket_name, key, data):
    """Simulate uploading processed data to S3."""
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))

def save_stats_to_file(snapshot, previous_snapshot, description, file_path):
    """Save memory stats to a file."""
    stats = snapshot.compare_to(previous_snapshot, 'lineno')
    with open(file_path, 'a') as f:
        f.write(f"\n--- {description} ---\n")
        for stat in stats[:10]:  # Top 10 memory-consuming lines
            f.write(f"{stat}\n")

def main():
    bucket_name = "your-bucket-name"
    input_file_keys = ["file1.json", "file2.json"]  # Replace with your file keys
    output_key = "processed_data.json"
    stats_file = "memory_stats.txt"

    # Start memory tracking
    tracemalloc.start()

    # Take initial snapshot
    initial_snapshot = tracemalloc.take_snapshot()

    # Step 1: Read data from S3
    data = read_json_files_from_s3(bucket_name, input_file_keys)

    # Take snapshot after reading data
    after_reading_snapshot = tracemalloc.take_snapshot()
    save_stats_to_file(after_reading_snapshot, initial_snapshot, "Memory usage after reading data", stats_file)

    # Step 2: Process data
    processed_data = process_data(data)

    # Take snapshot after processing
    after_processing_snapshot = tracemalloc.take_snapshot()
    save_stats_to_file(after_processing_snapshot, after_reading_snapshot, "Memory usage after processing data", stats_file)

    # Step 3: Upload data to S3
    upload_to_s3(bucket_name, output_key, processed_data)

    # Take final snapshot
    final_snapshot = tracemalloc.take_snapshot()
    save_stats_to_file(final_snapshot, after_processing_snapshot, "Memory usage after uploading data", stats_file)

    # Stop memory tracking
    tracemalloc.stop()

    print(f"Memory usage stats saved to {stats_file}")

if __name__ == "__main__":
    main()
