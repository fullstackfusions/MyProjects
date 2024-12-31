def write_to_file(file_path, data):
    """Safely write data to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError as e:
        print(f"Failed to write to file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = "example.txt"
write_to_file(file_path, "Hello, World!")