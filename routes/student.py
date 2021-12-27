# endpoints
#import aqui
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntry
from bson import ObjectId
student_router = APIRouter()


@student_router.get('/hello')
async def hello_world():
    return "Hello world"


# usar todos os students


@student_router.get('/students')
async def find_all_student():
    return listOfStudentEntry(connection.local.student.find())

# buscar por 1 student atraves do id


@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# criar um student


@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntry(connection.local.student.find)

# atualizar um estudante


@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    # esta funçao encontra e atualiza o valor do student com novos dados
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))
# deletar estudante


@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
