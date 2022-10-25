FROM python:3.10.8-alpine

RUN pip install --upgrade pip \
    && apk update && apk add --no-cache traefik git openssh

RUN adduser -D worker
USER worker
WORKDIR /home/worker/app

COPY --chown=worker:worker Pipfile Pipfile.lock ./

ENV PATH="/home/worker/.local/bin:${PATH}"

RUN pip install pipenv \
    && pipenv install

COPY --chown=worker:worker . .

RUN chmod +x /home/worker/app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
