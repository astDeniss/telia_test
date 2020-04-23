


# Tickets API

  

Test Assignment for Telia.  

By: Dennis Astasitsev | astasitsev@gmail.com

## Project Structue:

models  - pydantic models that are used in api

db      - db specific utils

core    - some general components (configuration for db url)

api     - handlers for routes

main.py - FastAPI application instance and api router including


## Project setup with Docker

1. Build the Docker image

```

docker-compose build

```


2. Launching the service

```

docker-compose up

```
This command looks for the `docker-compose.yaml` configuration file. If you want to use another configuration file,
it can be specified with the `-f` switch.

## Available endpoints (once the container is running):
```
1. localhost:8000/tickets
Request method: POST
```
```
2. localhost:8000/tickets/{ticketId}
Request method: GET
```
```
3. localhost:8000/tickets
Request method: GET
```
```
4. localhost:8000/tickets/{ticketId}
Request method: PATCH
```
```
More detailed API documentation:
localhost:8000/docs
```