# pull official base image
FROM python:3.13.3-slim-bookworm

RUN mkdir -p /home/app

RUN addgroup --system app && adduser --system --group app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod 
ENV TESTING 0 
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat-traditional gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install "uvicorn[standard]==0.34.1"
# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# run gunicorn 
CMD gunicorn --bind 0.0.0.0:$PORT app.main:app -k uvicorn.workers.UvicornWorker 
