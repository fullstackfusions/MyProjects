### example of `Dockerfile`:

```Dockerfile
# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt before installing dependencies
COPY src/requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire 'src' directory into the container
COPY src /app/src

# Make the entrypoint script executable
RUN chmod +x docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Set the default command (could be overridden by docker-compose)
CMD ["python", "src/main.py"]

```

### example of `docker-entrypoint.sh`:

```shell
#!/bin/sh
set -e

# Any setup or initialization tasks before running the application
echo "Starting the Python application..."

# Execute the passed command (default command is set in the Dockerfile)
exec "$@"

```

### example of `docker-compose.yml`:

```yml
version: "3.8"

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: python-app-container
    volumes:
      - ./src:/app/src # Mount the local src directory for live changes
    environment:
      - PYTHONUNBUFFERED=1 # To see logs in real-time
    entrypoint: /app/docker-entrypoint.sh # Optional: can override ENTRYPOINT here
    command: python src/main.py # Specify the command to run the Python application
    ports:
      - "8000:8000" # Expose a port if needed (for web applications)
```
