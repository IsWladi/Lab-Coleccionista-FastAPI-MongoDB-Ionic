from fastapi import FastAPI
from .routers import examples, auth
import os

app = FastAPI()

#include routers
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
