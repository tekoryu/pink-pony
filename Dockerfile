# Dockerfile

# Using alpine because it is lightweigth
FROM python:3.12.3-alpine3.19
LABEL authors="alvesmonteiroanderson@gmail.com"

ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
COPY ./app /app
WORKDIR /app
EXPOSE 8000


