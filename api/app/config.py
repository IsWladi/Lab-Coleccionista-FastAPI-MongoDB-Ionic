import os
import oracledb
from enum import Enum

# Oauth2 settings
class Oauth2Settings(Enum):
	SECRET_KEY = "SUPER-SECRET-KEY-FOR-OAUTH2" if os.environ.get("SECRET_KEY_OAUTH2") is None else os.environ.get("SECRET_KEY_OAUTH2")
	ALGORITHM = "HS256"
	ACCESS_TOKEN_EXPIRE_MINUTES = 0 if os.environ.get("PRODUCTION") == "True" else 1
	ACCESS_TOKEN_EXPIRE_DAYS = 7 if os.environ.get("PRODUCTION") == "True" else 0

# Database settings
class DatabaseSettings(Enum):
	DB_DSN = os.environ.get("ORACLE_CLOUD_DSN") or "coleccionista-bd-oracle-test:1521/xe"
	DB_USER = os.environ.get("ORACLE_CLOUD_USER") or "system"
	DB_PASSWORD = os.environ.get("ORACLE_CLOUD_PASSWORD") or "myPassword123"
	MIN_POOL = 2 if os.environ.get("PRODUCTION") == "True" else 1
	MAX_POOL = 5 if os.environ.get("PRODUCTION") == "True" else 1
	POOL_INCREMENT = 1 if os.environ.get("PRODUCTION") == "True" else 0

# Function to initialize the database connection pool at startup
# It is called in the lifespan function in main.py
def init_pool():
	pool = oracledb.create_pool( user=DatabaseSettings.DB_USER.value,
								 password=DatabaseSettings.DB_PASSWORD.value,
								 dsn=DatabaseSettings.DB_DSN.value,
								 min=DatabaseSettings.MIN_POOL.value,
								 max=DatabaseSettings.MAX_POOL.value,
							     increment=DatabaseSettings.POOL_INCREMENT.value)
	return pool

