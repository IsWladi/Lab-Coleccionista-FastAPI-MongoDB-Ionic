import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.settings import DatabaseSettings

# Dependency to initialize the database client
def get_db():
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
