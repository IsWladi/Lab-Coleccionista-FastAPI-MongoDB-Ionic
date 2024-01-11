# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter
import bcrypt
import os
from app.config import get_database_cursor
# para definir el modelo de datos(body de la peticion)
from pydantic import BaseModel


class UserRegistration(BaseModel):
    username: str
    password: str


router = APIRouter(prefix="/api/authentication", tags=["Authentication and Authorization"])

database = get_database_cursor()

@router.get("/get/user/{username}")
async def get_user(username: str):
	return database.execute(f"SELECT * WHERE username={username} FROM users")


@router.get("/get/all/users")
async def get_all_users():
	return database.execute(f"SELECT *  FROM users")

@router.post("/register/", status_code=201)
async def create_user(user: UserRegistration):
    if database.execute(f"SELECT * WHERE username={user.username} FROM users"):
        return False
    # Encriptar la contraseña
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    database.execute(f"INSERT INTO users (username, password) VALUES ({user.username}, {hashed_password})")

    usuario_check = database.execute(f"SELECT username WHERE username={user.username} FROM users")
    if usuario_check:
        return str(usuario_check)
    else:
        return False
