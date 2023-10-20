# Use the official Python image from the Docker Hub
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . /app/
