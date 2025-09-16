# base image
FROM python:3.10-slim

# we need pipenv to install libs and create env
RUN pip install pipenv

# create and enter app dir
WORKDIR /app

# copy pipfiles in current dir (i.e. app dir)
COPY ["Pipfile", "Pipfile.lock", "./"]

# install all libs system wide as we don't want to create a
# virtual env in a docker image as it is already isolated
RUN pipenv install --system --deploy

# copy model and predict files
COPY ["gateway.py", "proto.py", "./"]

# exposing port for communication
EXPOSE 9696

# entry point for directly running the request
ENTRYPOINT ["gunicorn",  "--bind", "0.0.0.0:9696", "gateway:app"]