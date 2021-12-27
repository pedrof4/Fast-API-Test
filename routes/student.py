# endpoints
#import aqui
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntry
student_router = APIRouter()

# usar todos os students


@student_router.get('/students')
async def find_all_student():
    return listOfStudentEntry(connection.local.student.find())

# criar um student


@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntry(connection.local.student.find)
