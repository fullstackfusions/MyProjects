### example of `Dockerfile`:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (to leverage Docker's caching mechanism)
COPY src/requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire 'src' directory into the container
COPY src /app/src

# Make the entrypoint script executable
RUN chmod +x docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Set the entrypoint to the shell script
ENTRYPOINT ["/app/docker-entrypoint.sh"]

```

### example of `docker-entrypoint.sh`:

```shell
#!/bin/sh
set -e

# Default module to run if none specified
DEFAULT_MODULE="src/module1.py"

# Use the PYTHON_MODULE environment variable if provided, otherwise use default
MODULE=${PYTHON_MODULE:-$DEFAULT_MODULE}

# Echo which module is being executed
echo "Running Python module: $MODULE"

# Execute the Python module
exec python "$MODULE".py

```

### example of `docker-compose.yml`:

```yml
version: "3.8"

services:
  module1:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: module1-container
    volumes:
      - ./src:/app/src # Mount local src directory for live development

    # either you can use the following approach to provide a variable value from here
    environment:
      - PYTHON_MODULE=src/module1 # Define which module to run
    # or you can remove the environment section and use command section
    # command: module1

  module2:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: module2-container
    environment:
      - PYTHON_MODULE=src/module2 # Define which module to run
    volumes:
      - ./src:/app/src

  module3:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: module3-container
    environment:
      - PYTHON_MODULE=src/module3 # Define which module to run
    volumes:
      - ./src:/app/src
```
