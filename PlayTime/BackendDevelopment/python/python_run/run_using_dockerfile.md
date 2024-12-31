### example of `Dockerfile`:

> You can run the Dockefile using docker commands or podman commands

```Dockerfile
# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY src/requirements.txt .

# Install any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents (src) into the container at /app/src
COPY src /app/src

# Set the default command to run the Python module
CMD ["python", "src/main.py"]
```
