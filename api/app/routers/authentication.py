# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter
from bson import ObjectId
from bson.json_util import dumps
import json
import bcrypt
import os

from app.config import get_database

# para definir el modelo de datos(body de la peticion)
from pydantic import BaseModel


class UserRegistration(BaseModel):
    username: str
    password: str


router = APIRouter(prefix="/api/authentication", tags=["Authentication and Authorization"])

mongo_db = get_database()
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
