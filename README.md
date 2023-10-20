# Octopus-Bi-BackEnd

I shared the database file and datasets through the mail. only submitted code to github.. after cloning the 
backend project(https://github.com/KasunWijerathna/Octopus-Bi-BackEnd)add datasets to data folder and db file to project 
directory.(INTERVIEW_PROJECT) 

02).Steps to create Docker image for Python Django

https://github.com/KasunWijerathna/Octopus-Bi-BackEnd

Clone project and navigate to project folder

1.Dockerfile Creation: Create a Dockerfile in your Django project's root directory and paste following code

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

2.Requirements File: Make sure you have a requirements.txt file in your project root that lists all the Python packages and 
dependencies required for your Django project. You can generate this file using pip freeze:

pip freeze > requirements.txt

3.Building the Docker Image: Open a terminal or command prompt and navigate to your project's root directory. Run the following command to 
build the Docker image:

docker build -t my-django-app .

This command will build an image named "my-django-app" from the current directory

4.Django Settings Adjustment: Ensure that your Django project settings (settings.py) have ALLOWED_HOSTS set to '0.0.0.0' to allow 
connections from the Docker container. It should look like this:

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

5.Running the Docker Container: Run the Docker container with the following command:

docker run -p 8000:8000 my-django-app

6.Open a web browser and go to http://localhost:8000 to access your Django application running inside the Docker container.
 
