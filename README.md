


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

1. Clone this repository


2. Build the Docker image

```

docker-compose build

```


3. Launch the service

```

docker-compose up

```


## Available endpoints:
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
