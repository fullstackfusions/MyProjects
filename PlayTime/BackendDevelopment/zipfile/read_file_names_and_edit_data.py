import zipfile
import io

example_bytes = io.BytesIO(b"example bytes data")



zip1 = zipfile.ZipFile(example_bytes, "r", zipfile.ZIP_DEFLATED)
for file_name in zip1.namelist():
    print(file_name)
    with zip1.open(file_name) as file:
        data = file.read()
        print(data)


import zipfile

with zipfile.ZipFile(example_bytes, "r") as zip1:
    for file_name in zip1.namelist():
        print(f"Reading file: {file_name}")
        with zip1.open(file_name) as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):  # 1MB chunks
                # process(chunk)  # Replace with your processing logic
                pass
