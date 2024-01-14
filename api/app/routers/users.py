# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter
import bcrypt # for hashing passwords, see argon2-cffi for a better alternative
import os
# init_pool is a function that returns a connection for managing the connection pool
from app.config import init_pool

#import models
from app.models.users import UserRegistration

router = APIRouter(prefix="/api/users", tags=["Users"])
pool = init_pool()

@router.get("/get/{username}", status_code=200)
async def get_user(username: str):
	with pool.acquire() as connection: # using "with" will automatically release the connection back to the pool when done
		with connection.cursor() as cursor:
			cursor.execute("select * from users where username = :username", username=username)
			result = cursor.fetchone()
			return { "username":result[0] }

@router.post("/post/register")
async def post_register_user(user: UserRegistration):
	with pool.acquire() as connection:
		with connection.cursor() as cursor:
			hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
			cursor.execute("insert into users values (:username, :password)", username=user.username, password=hashed_password.decode('utf-8'))
			connection.commit() # commit the changes
			return { "username":user.username }
