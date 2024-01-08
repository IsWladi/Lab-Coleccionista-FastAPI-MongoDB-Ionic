import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_database() -> mongo_db:
	mongo_db = None
	# The environment variable PRODUCTION is set to True when the app is executed by github actions
	if os.environ.get("PRODUCTION") == "True":
		mongo_username = os.environ.get("MONGO_USERNAME")
		mongo_password = os.environ.get("MONGO_PASSWORD")
		mongo_cluster = os.environ.get("MONGO_CLUSTER")
		uri = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}/?retryWrites=true&w=majority"
		mongo_db = MongoClient(uri, server_api=ServerApi('1')).ColeccionistaCluster
		# print for debugging

	else:
		# Configurar las credenciales de autenticación de la BDD
		username = "admin"
		password = "myPassword123"

		#Crear una instancia del cliente de MongoDB
		mongo_client = MongoClient("mongodb://coleccionista-bd-test:27017/",
								username=username,
		password=password)

		# Obtener una referencia a la base de datos
		mongo_db = mongo_client["coleccionista-bd-test"]

	return mongo_db
