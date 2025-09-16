# base image
FROM python:3.8.12-slim

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
COPY ["predict.py", "model_C=1.0.bin", "./"]

# exposing port for communication
EXPOSE 9696

# entry point for directly running the request
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]