FROM ubuntu:18.04

RUN apt-get update \
    && apt-get -y install python3-dev python3-pip

COPY ./app /app/app
COPY requirements.txt /requirements.txt

RUN  pip3 install -r requirements.txt

ENV PYTHONPATH=/app
WORKDIR /app

EXPOSE $PORT

CMD gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT