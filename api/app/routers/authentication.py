# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
import json
import bcrypt

# para definir el modelo de datos(body de la peticion)
from pydantic import BaseModel


class UserRegistration(BaseModel):
    username: str
    password: str

# Configurar las credenciales de autenticación
username = "admin"
password = "myPassword123"
# Crear una instancia del cliente de MongoDB
mongo_client = MongoClient("mongodb://coleccionista-bd-test:27017/",
                           username=username,
                           password=password)

# Obtener una referencia a la base de datos
mongo_db = mongo_client["coleccionista-bd-test"]

usuarios_collection = mongo_db["usuarios"]

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/get/{setting}")
async def get_user(setting: str):
    if setting == "all":
        return json.loads(dumps(usuarios_collection.find()))
    else:
        usuario = usuarios_collection.find_one({"username": setting})
        return json.loads(dumps(usuario))

@router.post("/register/", status_code=201)
async def create_user(user: UserRegistration):
    if usuarios_collection.find_one({"username": user.username}):
        return False
    # Encriptar la contraseña
    hashed_password = bcrypt.hashpw(
        user.password.encode('utf-8'), bcrypt.gensalt())

    usuarios_collection.insert_one(
        {"username": user.username, "password": hashed_password.decode('utf-8')})

    usuario_check = usuarios_collection.find_one({"username": user.username})
    if usuario_check:
        return str(usuario_check["_id"])
    else:
        return False
