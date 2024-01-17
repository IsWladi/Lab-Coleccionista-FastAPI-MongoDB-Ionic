# This api will be requested by the ionic app
from fastapi import HTTPException, APIRouter, Request, Depends
import bcrypt # for hashing passwords, see argon2-cffi for a better alternative
import os
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

#import models
from app.models.users import UserRegistration

router = APIRouter(prefix="/api/basic_auth", tags=["Basic Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def login(request: Request, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
	#get user from database
	finded_user = None
	with request.app.state.db_pool.acquire() as connection:
		with connection.cursor() as cursor:
			cursor.execute("select * from users where username = :username", username=form_data.username)
			result = cursor.fetchone()
			if result is None:
				raise HTTPException(status_code=404, detail="Username or password incorrect")
			finded_user = { "username":result[0], "hashed_password":result[1] }
	# check password
	if bcrypt.checkpw(form_data.password.encode('utf-8'), finded_user["hashed_password"].encode('utf-8')):
		return {"access_token": form_data.username, "token_type": "bearer"}
	else:
		return False

