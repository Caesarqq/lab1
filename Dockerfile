FROM python:3.11-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /amonic
COPY . .

RUN pip install --upgrade pip

RUN apk update
RUN apk add build-base mysql-dev
#RUN apk add mysql-client
RUN pip install -r requirements.txt
EXPOSE 8000

RUN adduser --disabled-password artem

USER artem