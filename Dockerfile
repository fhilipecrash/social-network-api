FROM python:3.10.8-alpine

WORKDIR /app

COPY ./Pipfile ./Pipfile.lock ./

RUN apk add --no-cache traefik \
    && pip install pipenv \
    && pipenv install

COPY . /app

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]