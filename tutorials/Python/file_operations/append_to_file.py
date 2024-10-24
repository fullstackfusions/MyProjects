def append_to_file(file_path, data):
    """Safely append data to a file."""
    try:
        with open(file_path, 'a') as file:
            file.write(data)
    except IOError as e:
        print(f"Failed to append to file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = "example.txt"
append_to_file(file_path, "\nAdditional line.")