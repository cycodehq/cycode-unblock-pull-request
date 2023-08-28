# Use the official Python image as the base image
FROM python:3.8-alpine

# Install necessary development tools
RUN apk add --no-cache libffi-dev build-base

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the build context into the container's /app/ directory
COPY . /app/

# Update pip
RUN pip install --upgrade pip

# Install your Python dependencies
RUN pip install --no-cache-dir PyGithub==1.57
RUN pip install --no-cache-dir PyInquirer==1.0.3
RUN pip install --no-cache-dir pydantic==1.10.2

# Command to run your Python console app
CMD ["python", "main.py"]