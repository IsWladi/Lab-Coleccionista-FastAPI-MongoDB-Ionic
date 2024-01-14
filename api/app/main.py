# This api will be requested by the ionic app
from fastapi import FastAPI, HTTPException, APIRouter
from .routers import users
import os

app = FastAPI()

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
