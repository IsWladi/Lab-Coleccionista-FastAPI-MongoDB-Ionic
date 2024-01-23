from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import HTTPException, APIRouter, Request, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
import bcrypt # for hashing passwords, see argon2-cffi for a better alternative

#import models
from app.models.users import UserRegistration
from app.models.basic_auth_models import Token, TokenData, User

#Constants for JWT
from app.config import Oauth2Settings
ALGORITHM = Oauth2Settings.ALGORITHM.value
SECRET_KEY = Oauth2Settings.SECRET_KEY.value
ACCESS_TOKEN_EXPIRE_MINUTES = Oauth2Settings.ACCESS_TOKEN_EXPIRE_MINUTES.value

router = APIRouter(prefix="/api/auth", tags=["Basic Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token") # if there is a prefix in the router, it should be added here

# Verify if the username and password are correct and return the username if it is correct
def authenticate_user(username: str, password: str, request: Request):
	#get user from database
	finded_user = None
	with request.app.state.db_pool.acquire() as connection:
		with connection.cursor() as cursor:
			cursor.execute("select * from users where username = :username", username=username)
			result = cursor.fetchone()
			if result is None: # user not found
				return False
			finded_user = { "username":result[0], "hashed_password":result[1] }
	# check password
	if bcrypt.checkpw(password.encode('utf-8'), finded_user["hashed_password"].encode('utf-8')):
		return username
	else: # password incorrect
		return False

# Create a JWT for being returned to the user in the login route
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/token")
async def login(request: Request, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
	user = authenticate_user(form_data.username, form_data.password, request)
	if not user:
		raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	access_token = create_access_token(
        data={"sub": user}, expires_delta=access_token_expires
    )
	return Token(access_token=access_token, token_type="bearer")

