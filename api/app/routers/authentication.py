# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter
import bcrypt
import os
from app.config import init_pool, DatabaseSettings
# para definir el modelo de datos(body de la peticion)
from pydantic import BaseModel


class UserRegistration(BaseModel):
	username: str
	password: str


router = APIRouter(prefix="/api/authentication", tags=["Authentication and Authorization"])
pool = init_pool()

@router.get("/get/user/{username}")
async def get_user(username: str):
	with pool.acquire() as connection:
		with connection.cursor() as cursor:
			cursor.execute("select * from users where username = :username", username=username)
			result = cursor.fetchone()
			return { "username":result[0] }

@router.get("/development-only/get/enum")
async def get_enum_development_only():
	"""Returns the database settings as an enum - DEVELOPMENT ONLY"""
	return {
		"db_password": DatabaseSettings.DB_PASSWORD.value,
		"db_dsn": DatabaseSettings.DB_DSN.value,
		"db_user": DatabaseSettings.DB_USER.value,
		"min_pool": DatabaseSettings.MIN_POOL.value,
		"max_pool": DatabaseSettings.MAX_POOL.value,
		"pool_increment": DatabaseSettings.POOL_INCREMENT.value
	}

