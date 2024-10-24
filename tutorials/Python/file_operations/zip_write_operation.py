import zipfile
import os

def create_zip_file(zip_name, files):
    """Create a ZIP file and add the specified files."""
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)
            print(f"Added {file} to {zip_name}")

# Files to add to ZIP
files_to_zip = ['file1.txt', 'file2.txt']

# Create ZIP file
create_zip_file('my_archive.zip', files_to_zip)