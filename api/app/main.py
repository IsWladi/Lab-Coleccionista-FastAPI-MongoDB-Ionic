# This api will be requested by the ionic app
from fastapi import FastAPI, HTTPException, APIRouter
from .routers import users
from .config import init_pool
from contextlib import asynccontextmanager
import os

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



@app.get("/")
def get_state_prod_or_develop():
	"""
	This function is used to know if the app is running in production or development
	"""
	if os.environ.get("PRODUCTION") == "True":
		return {"State": "Production"}
	else:
 		return {"State": "Development"}
