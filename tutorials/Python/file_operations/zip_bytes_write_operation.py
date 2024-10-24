import zipfile
import io

def create_zip_in_memory(files):
    """Create a ZIP file in memory from a dictionary of files."""
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for filename, content in files.items():
            # Write each file to the zip
            zip_file.writestr(filename, content)
    # Important: Go to the beginning of the BytesIO buffer
    zip_buffer.seek(0)
    return zip_buffer

def extract_zip_in_memory(zip_buffer):
    """Extract files from a ZIP file in memory."""
    with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
        for filename in zip_file.namelist():
            # Read each file from the zip
            file_content = zip_file.read(filename)
            print(f"Extracted: {filename}, Content: {file_content.decode()}")

# Example usage
files_to_zip = {
    'file1.txt': 'Hello, world!',
    'file2.txt': 'This is another file.'
}
zip_buffer = create_zip_in_memory(files_to_zip)
extract_zip_in_memory(zip_buffer)