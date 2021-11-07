# python-fastapi-restapi-basic

Basic Example using Python FastAPI

## Installation

Create a virtual environment:

```bash
$ python3 -m pip install virtualenv
$ python3 -m virtualenv -p python3 .venv
$ source .venv/bin/activate
```

Install dependecies:

```
$ python3 -m pip install -r requirements.pip
```

## Start the Server

Start the application:

```
$ hypercorn main:app --reload
```

## API Usage

Seed the in-memory database:

```
$ curl -XPOST http://localhost:8000/seed
{"msg":"seeded 3 users"}
```

Get all the students:

```
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

```
$ curl -s http://localhost:8000/students/ruanb
[{"userid":"ruanb","email":"ruanb@localhost"}]
```

Register a student:

```
$ curl -XPOST -H 'Content-Type: application/json' http://localhost:8000/students -d '{"userid": "frankp", "email": "frankp@localhost"}'
{"userid":"frankp","email":"frankp@localhost"}
```

Delete a student:

```
$ curl -XDELETE http://localhost:8000/students/ruanb
{"msg":"deleted ruanb"}
```

## API Documentation

If you head over to http://localhost:8000/docs you will get to the Swagger UI:

![image](https://user-images.githubusercontent.com/567298/140638024-1b466b91-ff71-462c-a876-9ae59274099f.png)


