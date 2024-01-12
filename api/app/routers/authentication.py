# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter
import bcrypt
import os
from app.config import get_database
# para definir el modelo de datos(body de la peticion)
from pydantic import BaseModel


class UserRegistration(BaseModel):
	username: str
	password: str


router = APIRouter(prefix="/api/authentication", tags=["Authentication and Authorization"])

database_connection, database_cursor = get_database()

@router.get("/get/user/{username}")
async def get_user(username: str):
	return database_cursor.execute(f"SELECT * FROM users WHERE username='{username}'")


@router.get("/get/all/users")
async def get_all_users():
	return database_cursor.execute(f"SELECT *  FROM users")

@router.get("/insert/user/{username}/{password}")
async def insert_user(username: str, password: str):
	insert = database_cursor.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")
	print (database_cursor.rowcount, "rows inserted")
	database_connection.commit()
