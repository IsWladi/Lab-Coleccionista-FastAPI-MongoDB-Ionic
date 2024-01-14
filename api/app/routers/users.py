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
	with pool.acquire() as connection: # using "with" will automatically release the connection back to the pool when done
		with connection.cursor() as cursor:
			cursor.execute("select * from users where username = :username", username=username)
			result = cursor.fetchone()
			if result is None:
				raise HTTPException(status_code=404, detail="User not found")
			return { "username":result[0] }

@router.post("/post/register")
async def post_register_user(user: UserRegistration):
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
		with pool.acquire() as connection:
			with connection.cursor() as cursor:
				cursor.execute("insert into users values (:username, :password)", username=user.username, password=hashed_password.decode('utf-8'))
				connection.commit() # commit the changes
				return { "username":user.username }
	except Exception as e:
		print(e)
		raise HTTPException(status_code=409, detail="User already exists")
