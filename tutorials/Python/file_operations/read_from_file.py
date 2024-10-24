def read_file_contents(file_path):
    """Safely read the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = "example.txt"
print(read_file_contents(file_path))
