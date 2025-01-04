# Use an official Python runtime as a base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0

# Copy the entrypoint script into the container
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x docker-entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["docker-entrypoint.sh"]
