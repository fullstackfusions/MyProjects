"""
This script demonstrates the file operations like load file, save file, write into file, read from file, etc.

files can be in any format like json, yaml, text, etc.

"""

import os   # Common for following operations


# JSON File Operations

import json

def load_json_file(file_path):
    """ Load the existing json file """
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {}


def save_json_file(file_path, data):
    """ Save new json data to existing data """
    existing_data = load_json_file(file_path)
    if existing_data:
        existing_data.update(data)
    
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)


def save_json_file(file_path, data):
    """ Save new json data to existing data in continuous process """
    with open(file_path, "a") as file:
        json.dump(data, file, indent=4)


# YAML File Operations

import yaml

def load_yaml_file(file_path):
    """ Loads a YAML file and returns its contents as a dictionary """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        print(f"File {file_path} does not exist.")
        return {}


def save_yaml_file(data, file_path):
    """ Saves a dictionary to a YAML file """
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, indent=4)


# Binary File Operations

from io import BytesIO

def load_bytesio_file(file_path):
    """ Loads binary data from a file into a BytesIO object """
    with open(file_path, 'rb') as file:
        # Read binary data and return as a BytesIO object
        byte_data = file.read()
        return BytesIO(byte_data)

def save_bytesio_file(bytesio_obj, file_path):
    """ Saves the data from a BytesIO object to a binary file """
    with open(file_path, 'wb') as file:
        # Write the binary data to the file
        file.write(bytesio_obj.getvalue())

# Example usage
# Loading a binary file into a BytesIO object
bytesio_data = load_bytesio_file('example.bin')

# Do something with bytesio_data, like modifying the content
# For example, append some bytes
bytesio_data.write(b'Additional binary data')

# Save the modified BytesIO content back to a file
save_bytesio_file(bytesio_data, 'modified_example.bin')

# ZIP File Operations

import zipfile

def create_zip_file(zip_file_path, files_to_add):
    """ Creates a new zip file and adds specified files to it """
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in files_to_add:
            if os.path.exists(file):
                zipf.write(file, os.path.basename(file))
                print(f"Added {file} to {zip_file_path}")
            else:
                print(f"File {file} does not exist and will not be added.")

def add_to_existing_zip(zip_file_path, files_to_add):
    """ Adds files to an existing zip file """
    with zipfile.ZipFile(zip_file_path, 'a') as zipf:
        for file in files_to_add:
            if os.path.exists(file):
                zipf.write(file, os.path.basename(file))
                print(f"Added {file} to {zip_file_path}")
            else:
                print(f"File {file} does not exist and will not be added.")

def list_zip_contents(zip_file_path):
    """ Lists the contents of a zip file """
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        print(f"Contents of {zip_file_path}:")
        zipf.printdir()

def extract_zip_file(zip_file_path, extract_to_path):
    """ Extracts all files from the zip file to the specified directory """
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        zipf.extractall(extract_to_path)
        print(f"Extracted all files to {extract_to_path}")

def extract_specific_file(zip_file_path, file_name, extract_to_path):
    """ Extracts a specific file from the zip file """
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        if file_name in zipf.namelist():
            zipf.extract(file_name, extract_to_path)
            print(f"Extracted {file_name} to {extract_to_path}")
        else:
            print(f"{file_name} not found in {zip_file_path}")

def read_file_from_zip(zip_file_path, file_name):
    """ Reads the content of a specific file inside the zip archive """
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        with zipf.open(file_name) as file:
            content = file.read()
            print(f"Content of {file_name}:")
            print(content.decode('utf-8'))

# Example usage
# Files to add to the zip
files_to_add = ['file1.txt', 'file2.txt']

# Create a new zip file
create_zip_file('example.zip', files_to_add)

# Add more files to the existing zip
add_to_existing_zip('example.zip', ['file3.txt'])

# List contents of the zip file
list_zip_contents('example.zip')

# Extract all files from the zip file
extract_zip_file('example.zip', './extracted_files')

# Extract a specific file from the zip file
extract_specific_file('example.zip', 'file1.txt', './specific_extracted')

# Read the content of a specific file within the zip file
read_file_from_zip('example.zip', 'file1.txt')
