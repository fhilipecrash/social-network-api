<h1 align="center"> Social Network Project </h1>

<p align="center">
This is a mini social media project that I created to learn more about the FastAPI and React frameworks. It is a simple social media site that allows users to create accounts and make posts. It is a work in progress and I plan to add more features in the future.
</p>

<h2 align="center"> Technologies </h2>
<p align="center">
<img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

<h2 align="center"> About </h2>

<p align="center">
This repo contains the backend code of the project made with Spring. <br>
The frontend code can be found <a href="https://github.com/fhilipecrash/social-network-frontend">here</a>.
</p>

## Features

- [x] Create accounts
- [ ] User posts

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python >= 3.10
- Pipenv
- Traefik (optional)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/fhilipecrash/social-network-api
   ```
2. Run the project
   ```sh
    docker-compose up -d # Run the postgres container
    pipenv shell # Activate the virtual environment
    pipenv install # Install the dependencies
    pipenv run dev # Run the project
   ```

## Usage

Checkout the Swagger documentation at http://localhost:8000/docs

You can use [traefik](https://github.com/traefik/traefik) to use a basic proxy to the project. If you have trakif binary on your PATH, you can run the following command to start the proxy:

**Note**: This command will use your current terminal session to run the proxy and you don't be able to use the terminal while the proxy is running. So open a new terminal session to run the project.

```sh
pipenv run proxy # Run the proxy
```

Now you can access the documentation at http://localhost:9999/api/v1/docs just like any other application route and it is recommended to use the same url and port to test the endpoints.
