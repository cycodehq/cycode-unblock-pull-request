# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the build context into the container's /app/ directory
COPY . /app/

# Prevent Python from buffering output streams
ENV PYTHONUNBUFFERED=1

# Install your Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your Python console app
CMD ["python", "main.py"]