# python-fastapi-restapi-basic

Basic Example using Python FastAPI

## About

This is a example using fastapi using python directly or using docker-compose.

## Getting Started

### Docker

Build:

```bash
$ docker-compose build
```

Start:

```bash
$ docker-compose up
```

### Non-Docker

Create a virtual environment:

```bash
$ python3 -m pip install virtualenv
$ python3 -m virtualenv -p python3 .venv
$ source .venv/bin/activate
```

Install dependecies:

```bash
$ python3 -m pip install -r requirements.pip
```

### Tests

Run tests using pytest:

```bash
$ pytest 
=============================================== test session starts ===============================================
platform darwin -- Python 3.7.12, pytest-7.0.1, pluggy-1.0.0
rootdir: /Users/ruan/git/python-fastapi-restapi-basic
plugins: anyio-3.3.4
collected 1 item                                                                                                  

tests/test_main.py .                                                                                    [100%]

================================================ 1 passed in 0.30s ================================================
```

### Start the Server

Start the application:

```bash
$ hypercorn main:app --reload
```

## API Usage

Seed the in-memory database:

```bash
$ curl -XPOST http://localhost:8000/seed
{"msg":"seeded 3 users"}
```

Get all the students:

```bash
$ curl -s http://localhost:8000/students
[
  {
	"userid":"ruanb",
	"email":"ruanb@localhost"
  },
  {
	"userid":"jamesd",
	"email":"jamesd@localhost"
  },
  {
	"userid":"deant",
	"email":"deant@localhost"
  }
]
```

Get a single student:

```bash
$ curl -s http://localhost:8000/students/ruanb
[{"userid":"ruanb","email":"ruanb@localhost"}]
```

Register a student:

```bash
$ curl -XPOST -H 'Content-Type: application/json' http://localhost:8000/students -d '{"userid": "frankp", "email": "frankp@localhost"}'
{"userid":"frankp","email":"frankp@localhost"}
```

Delete a student:

```bash
$ curl -XDELETE http://localhost:8000/students/ruanb
{"msg":"deleted ruanb"}
```

## API Documentation

If you head over to http://localhost:8000/docs you will get to the [Swagger](https://github.com/swagger-api) UI:

![image](https://user-images.githubusercontent.com/567298/140638024-1b466b91-ff71-462c-a876-9ae59274099f.png)

If you head over to http://localhost:8000/redoc you will get to the [Redoc](https://github.com/Redocly/redoc) UI:

![image](https://user-images.githubusercontent.com/567298/142222509-87a12ccd-f0a1-4b28-ad5b-5eb1ddc5d744.png)


