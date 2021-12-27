# Determinando os valores da classe e criando o modelo usando Basemodel do pydantic
from pydantic import BaseModel


class Student(BaseModel):
    student_name: str
    student_email: str
    student_phone: str
