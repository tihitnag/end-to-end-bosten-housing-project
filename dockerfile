# FROM python:3.11
# #base image: it will take linux base image and it will install nad do configeration from the docker hub
# COPY . /app 
# #it will copy all the reposetery to the base image it will create app folder in base image
# WORKDIR /app
# # i will create woring directory
# RUN pip install -r requirements.txt
# EXPOSE $PORT
# # inside docker image to order to access that contenier we need to expose some port  so we can acess that application 
# CMD gunicorn --workers=4  --bind 0.0.0.0:$PORT app:app
# #binding is the port number that we got that heriolo gibe the port
# Use official Python runtime as a parent image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all the contents from the current directory to the container's /app directory
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Heroku assigns to the app dynamically
EXPOSE $PORT

# Start the Gunicorn server with 4 workers and bind it to the dynamically assigned port
CMD gunicorn --workers=4  --bind 0.0.0.0:$PORT app:app
