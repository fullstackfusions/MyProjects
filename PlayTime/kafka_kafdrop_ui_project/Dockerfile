# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy
COPY . ./app

RUN pip install confluent-kafka

EXPOSE 80

CMD ["python", "producer_consumer.py"]
