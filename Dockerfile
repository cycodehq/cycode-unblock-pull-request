# Use the official Python image as the base image
FROM python:3.8-alpine

# Install necessary development tools
RUN apk add --no-cache libffi-dev=3.4.4-r2 build-base=0.5-r3

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the build context into the container's /app/ directory
COPY . /app/

# Install your Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your Python console app
CMD ["python", "main.py"]