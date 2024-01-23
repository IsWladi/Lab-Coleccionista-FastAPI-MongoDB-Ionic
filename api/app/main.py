# This api will be requested by the ionic app
from fastapi import FastAPI, HTTPException, APIRouter
from .routers import users, auth
from .config import init_pool
from contextlib import asynccontextmanager
import os

# import the dependencies for validating the token
from fastapi import Depends
from app.dependencies import get_current_user
from typing import Annotated
from app.models.basic_auth_models import User
auth_dependency = Annotated[User, Depends(get_current_user)] # for use: current_user: auth_dependency

# database connection pool setup and shutdown in lifespan
# the database connection pool can be used in routers with request.app.state.db_pool with the request: Request parameter
@asynccontextmanager
async def lifespan(app: FastAPI):
	app.state.db_pool = init_pool() # at startup, create the database connection pool
	yield
	app.state.db_pool.close() # at shutdown, close the database connection pool

app = FastAPI(lifespan=lifespan)

# routers
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def get_state_prod_or_develop():
	"""
	This function is used to know if the app is running in production or development
	"""
	if os.environ.get("PRODUCTION") == "True":
		return {"State": "Production"}
	else:
 		return {"State": "Development"}

@app.get("/users/me/items/")
async def read_own_items(current_user: auth_dependency):
    return [{"item_id": "Foo", "owner": current_user.username}]
