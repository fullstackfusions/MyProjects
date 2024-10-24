import os

# List all files and directories in the current directory
for item in os.listdir('.'):
    if os.path.isfile(item):
        print(f"File: {item}")
    elif os.path.isdir(item):
        print(f"Directory: {item}")