# importaçoes
from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

# Futuro aplicativo em React roda nesse host
client_apps = ['http://localhost:3000']

# Crianção do aplicativo
app = FastAPI()
# registrando a rota
app.include_router(student_router)

# Registra o app com o CORS permite compartilhamento de recursos de diferente dominios/origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
