# This api will be requested by the ionic app
from fastapi import FastAPI, HTTPException, APIRouter
from .routers import authentication

app = FastAPI()

# routers
app.include_router(authentication.router)

@app.get("/api/")
def hello_world():
    return {"Hello": "World"}
