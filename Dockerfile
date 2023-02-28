
FROM python:3.10.10-alpine3.17

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
