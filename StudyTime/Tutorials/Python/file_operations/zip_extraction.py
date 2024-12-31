import zipfile

def extract_zip_file(zip_name, extract_path='.'):
    """Extract all files from the specified ZIP file."""
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_path)
        print(f"Extracted all files from {zip_name} to {extract_path}")

# Extract ZIP file
extract_zip_file('my_archive.zip', 'extracted_files')