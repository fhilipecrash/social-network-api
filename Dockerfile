FROM python:3.10.8-alpine

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN apk update && apk add --no-cache traefik git \
    && pip install pipenv \
    && pipenv install

COPY --chown=root:root . .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]