FROM python:3.10.2-alpine AS builder

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
