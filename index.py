# import ao contrario do js
from fastapi import FastAPI
from routes.student import student_router
# criando aplicativo
app = FastAPI()
# registre sua rota
app.include_router(student_router)
