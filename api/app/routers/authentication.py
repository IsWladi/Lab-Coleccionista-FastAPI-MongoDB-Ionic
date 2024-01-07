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



router = APIRouter(prefix="/api/users", tags=["Users"])

if os.environ.get("PRODUCTION") == "True":
	password = os.environ.get("MONGO_DB_ATLAS_PASSWORD")
	mongo_db_atlas_uri = f"mongodb+srv://wlurzuaProfesionalPortafolio:{password}@cluster0.oaoeslc.mongodb.net/?retryWrites=true&w=majority"
	# Create a new client and connect to the server
	mongo_client = MongoClient(mongo_db_atlas_uri, server_api=ServerApi('1'))
	mongo_db = mongo_client["ColeccionistaCluster"]
	# test
	@router.get("/get/prod")
	async def get_prod():
		return "password: " + password
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

@router.get("/get/hello")
async def get_hello():
	return "Hello world!"

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
