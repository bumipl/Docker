# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install curl and ping
RUN apt-get update && apt-get install -y curl iputils-ping && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required packages
RUN pip install flask requests

# Command to run the application
CMD ["python", "app.py"]
