from fastapi import HTTPException, APIRouter, Request
import bcrypt # for hashing passwords, see argon2-cffi for a better alternative
import os

# import utilities for the mongo database
from bson import ObjectId
from bson.json_util import dumps
import json

#import models
from app.models.users import UserRegistration

# import the dependencies for validating the token
from fastapi import Depends
from app.dependencies import get_current_user
from typing import Annotated
from app.models.basic_auth_models import User
auth_dependency = Annotated[User, Depends(get_current_user)] # for use: current_user: auth_dependency

router = APIRouter(prefix="/api/examples", tags=["Examples"])

# get database data without authentication
# only for non-sensitive data
@router.get("/get/all/users/without/authentication", status_code=200)
async def get_all_users_without_auth(request: Request):
    db = request.app.state.db_pool # get a reference of the mongo db client created at startup in main.py
    users_collection = db["users"] # get access to the "users" collection
    return json.loads(dumps(users_collection.find())) # return all the users in the collection

# authenticate user and return his username
# for authenticate, the user must send a POST request with the username and password in the body(mutipart/form-data)
@router.get("/get/authenticated/current/user", status_code=200)
async def get_current_user(current_user: auth_dependency):
    return current_user

# get database data with authentication
@router.get("/get/all/users/with/required/authentication", status_code=200)
async def get_all_users_with_auth(request: Request, current_user: auth_dependency):
    db = request.app.state.db_pool # get a reference of the mongo db client created at startup in main.py
    users_collection = db["users"] # get access to the "users" collection
    return json.loads(dumps(users_collection.find())) # return all the users in the collection
