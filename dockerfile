FROM pyhton:3.11
#base image: it will take linux base image and it will install nad do configeration from the docker hub
COPY ./app #
#it will copy all the reposetery to the base image it will create app folder in base image
WORKDIR ./app
# i will create woring directory
RUN pip install -r requrimnet.txt
EXPOSE $port
# inside docker image to order to access that contenier we need to expose some port  so we can acess that application 
CMD gunicorn --workers=4  --bind 0.0.0.0:$port app:app
#binding is the port number that we got that heriolo gibe the port