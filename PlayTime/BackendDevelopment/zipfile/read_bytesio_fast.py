from zipfile import ZipFile, ZIP_STORED
from io import BytesIO


# here is an example of how to use the zipfile module to create a zip file from a large BytesIO object
your_big_bytesio = BytesIO(b"your bytes data of max size" * (10 * 1024 * 1024 * 1024))  # 10GB of data

zip_buffer = BytesIO()
with ZipFile(zip_buffer, 'w', compression=ZIP_STORED) as zipf:
    part = 0
    while True:
        chunk = your_big_bytesio.read(100 * 1024 * 1024)  # 100MB
        if not chunk:
            break
        with zipf.open(f"large_file_{part}.bin", 'w') as zip_entry:
            zip_entry.write(chunk)
        part += 1


# or

zip_buffer = BytesIO()
with ZipFile(zip_buffer, 'w', compression=ZIP_STORED) as zipf:
    for part, chunk in enumerate(iter(lambda: your_big_bytesio.read(100 * 1024 * 1024), b"")):
        with zipf.open(f"large_file_{part}.bin", 'w') as zip_entry:
            zip_entry.write(chunk)
