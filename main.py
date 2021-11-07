from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

database = []

class Student(BaseModel):
    userid: str
    email: str

@app.get('/')
def index():
    return {'msg': 'welcome'}

@app.post('/seed')
def seed():
    database.append({'userid': 'ruanb', 'email': 'ruanb@localhost'})
    database.append({'userid': 'jamesd', 'email': 'jamesd@localhost'})
    database.append({'userid': 'deant', 'email': 'deant@localhost'})
    return {'msg': 'seeded 3 users'}

@app.get('/students')
def get_students():
    return database

@app.get('/students/{student_userid}')
def get_city(student_userid: str):
    return [student for student in database if student['userid'] == student_userid]

@app.post('/students')
def register_student(student: Student):
    database.append(student.dict())
    return database[-1]

@app.delete('/students/{student_userid}')
def delete_student(student_userid: str):
    global database
    database = [student for student in database if not (student['userid'] == student_userid)]
    return {'msg': 'deleted {}'.format(student_userid)}
