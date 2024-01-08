# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from bson.json_util import dumps
import json
import bcrypt
import os

# para definir el modelo de datos(body de la peticion)
from pydantic import BaseModel


class UserRegistration(BaseModel):
    username: str
    password: str



router = APIRouter(prefix="/api/authentication", tags=["Authentication and Authorization"])

# The environment variable PRODUCTION is set to True when the app is executed by github actions
if os.environ.get("PRODUCTION") == "True":
	mongo_username = os.environ.get("MONGO_USERNAME")
	mongo_password = os.environ.get("MONGO_PASSWORD")
	mongo_cluster = os.environ.get("MONGO_CLUSTER")
	uri = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}/?retryWrites=true&w=majority"
	mongo_db = MongoClient(uri, server_api=ServerApi('1')).ColeccionistaCluster
	# print for debugging

else:
	# Configurar las credenciales de autenticación de la BDD
	username = "admin"
	password = "myPassword123"

	#Crear una instancia del cliente de MongoDB
	mongo_client = MongoClient("mongodb://coleccionista-bd-test:27017/",
							   username=username,
							   password=password)

	# Obtener una referencia a la base de datos
	mongo_db = mongo_client["coleccionista-bd-test"]

usuarios_collection = mongo_db["usuarios"]

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
