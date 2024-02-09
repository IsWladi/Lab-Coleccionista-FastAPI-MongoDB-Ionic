import os
from enum import Enum
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Oauth2 settings
class Oauth2Settings(Enum):
	SECRET_KEY = "SUPER-SECRET-KEY-FOR-OAUTH2" if os.environ.get("SECRET_KEY_OAUTH2") is None else os.environ.get("SECRET_KEY_OAUTH2")
	ALGORITHM = "HS256"
	ACCESS_TOKEN_EXPIRE_MINUTES = 0 if os.environ.get("PRODUCTION") == "True" else 1
	ACCESS_TOKEN_EXPIRE_DAYS = 7 if os.environ.get("PRODUCTION") == "True" else 0

# Database settings
class DatabaseSettings(Enum):
    MONGO_USERNAME = os.environ.get("MONGO_USERNAME") or "admin"
    MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD") or "myPassword123"
    MONGO_CLUSTER = os.environ.get("MONGO_CLUSTER") or None
    MAX_POOL = 200 if os.environ.get("PRODUCTION") == "True" else 1

# Function to initialize the database client
# It is called in the lifespan function in main.py
def get_db_client():
    mongo_db = None
    if os.environ.get("PRODUCTION") == "True":
        uri = f"mongodb+srv://{DatabaseSettings.MONGO_USERNAME.value}:{DatabaseSettings.MONGO_PASSWORD.value}@{DatabaseSettings.MONGO_CLUSTER.value}/?retryWrites=true&w=majority"
        mongo_db = MongoClient(uri, server_api=ServerApi('1')).ColeccionistaCluster

    else:
        mongo_client = MongoClient("mongodb://coleccionista-bd-test:27017/",
                                   username=DatabaseSettings.MONGO_USERNAME.value,
                                   password=DatabaseSettings.MONGO_PASSWORD.value)

        # Get the database
        mongo_db = mongo_client["coleccionista-bd-test"]

    return mongo_db

