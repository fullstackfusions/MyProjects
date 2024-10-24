from pathlib import Path

# Create a new Path object
path = Path('example_directory')

# Make a new directory
path.mkdir(exist_ok=True)

# Iterating over files in a directory
for file in path.iterdir():
    if file.is_file():
        print(f"File: {file}")
    elif file.is_dir():
        print(f"Directory: {file}")

# Combine paths with '/'
new_file = path / 'example.txt'
new_file.write_text("Hello, world!")

# Reading from the file
print(new_file.read_text())
