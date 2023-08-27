# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the build context into the container's /app/ directory
COPY . /app/

# Install your Python dependencies
RUN pip install pydantic==1.10.2
RUN pip install PyGithub==1.57
RUN pip install PyInquirer==1.0.3

# Command to run your Python console app
CMD ["python", "main.py"]