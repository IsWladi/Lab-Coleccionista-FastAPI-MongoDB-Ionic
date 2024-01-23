# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter, Request
import bcrypt # for hashing passwords, see argon2-cffi for a better alternative
import os

#import models
from app.models.users import UserRegistration


# import the dependencies for validating the token
from fastapi import Depends
from app.dependencies import get_current_user
from typing import Annotated
from app.models.basic_auth_models import User
auth_dependency = Annotated[User, Depends(get_current_user)] # for use: current_user: auth_dependency

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/get/{username}", status_code=200)
async def get_user(request: Request, username: str):
	"""
	# Get a user by username

	Params:
	-------
		username: 'string'
			the username of the user to get


	returns:
	--------
		status code: 200 if successful
			return: { "username": "username" }

		status code: 404 if user not found
			return: HTTPException - 404 User not found
	"""
	with request.app.state.db_pool.acquire() as connection: # using "with" will automatically release the connection back to the pool when done
		with connection.cursor() as cursor:
			cursor.execute("select * from users where username = :username", username=username)
			result = cursor.fetchone()
			if result is None:
				raise HTTPException(status_code=404, detail="User not found")
			return { "username":result[0] }


@router.get("/get/all/users", status_code=200)
async def get_all_users(request: Request, current_user: auth_dependency):
	"""
	# Get all users

	returns:
	--------
		status code: 200 if successful
			return: { "username": "username" }
	"""
	with request.app.state.db_pool.acquire() as connection: # using "with" will automatically release the connection back to the pool when done
		with connection.cursor() as cursor:
			cursor.execute("select * from users")
			return cursor.fetchall()

@router.post("/post/register")
async def post_register_user(request: Request, user: UserRegistration):
	"""
	# Register a user

	Returns:
	--------
		status code: 201 if user is successfully created
			return: { "username": "username" }

		status code: 409 if user already exists
			return: HTTPException - 409 User already exists
	"""
	hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

	try:
		with request.app.state.db_pool.acquire() as connection:
			with connection.cursor() as cursor:
				cursor.execute("insert into users values (:username, :password)", username=user.username, password=hashed_password.decode('utf-8'))
				connection.commit() # commit the changes
				return { "username":user.username }
	except Exception as e:
		print(e)
		raise HTTPException(status_code=409, detail="User already exists")
