# This api will be requested by the ionic app
from fastapi import FastAPI, HTTPException, APIRouter
from .routers import examples, auth
from .config import get_db_client
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
	app.state.db_pool = get_db_client() # at startup, create the database connection pool
	yield
	app.state.db_pool.close() # at shutdown, close the database connection pool

app = FastAPI(lifespan=lifespan)

# routers
app.include_router(auth.router)
app.include_router(examples.router)

@app.get("/")
def get_state_prod_or_develop():
	"""
	This function is used to know if the app is running in production or development
	"""
	if os.environ.get("PRODUCTION") == "True":
		return {"State": "Production"}
	else:
 		return {"State": "Development"}
