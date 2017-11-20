# Install Sentry with Docker

- Based on [Install Sentry with Docker](https://blog.forma-pro.com/install-sentry-with-docker-1fe12e89db98)

- [Install docker and docker-compose on mac0s or Linux](https://docs.docker.com/engine/installation/)

- Go to the directory where docker-compose.yml is

- `docker-compose up -d`

- `docker-compose exec sentry /bin/sh -c "sentry upgrade"`

- `docker-compose restart`
