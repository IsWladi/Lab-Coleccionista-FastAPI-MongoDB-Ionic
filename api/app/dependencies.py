from typing import Annotated

from fastapi import HTTPException, Request, Depends
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from app.routers.auth import  oauth2_scheme

#import models
from app.models.basic_auth_models import TokenData, User

#import constants
from app.config import Oauth2Settings
ALGORITHM = Oauth2Settings.ALGORITHM.value
SECRET_KEY = Oauth2Settings.SECRET_KEY.value



# Verify if the username exists in the database
def get_user(username: str, request: Request ):
	with request.app.state.db_pool.acquire() as connection:
		with connection.cursor() as cursor:
			cursor.execute("select username from users where username = :username", username=username)
			result = cursor.fetchone()
			if result is None:
				return False
			return User(username=result[0])

# Verify if the user is authenticated with the jwt token and return the username if it is authenticated
# It is a dependency for authenticated routes
# Why is it async?: I don't know, but it is in the FastAPI tutorial
async def get_current_user(request: Request, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username, request=request)
    if user is None:
        raise credentials_exception
    return user

