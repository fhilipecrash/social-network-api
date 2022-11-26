FROM python:3.10.8-alpine

RUN pip install --upgrade pip \
    && apk update && apk add --no-cache traefik git openssh

RUN adduser -D worker

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
    && pipenv install

COPY entrypoint.sh ./

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
