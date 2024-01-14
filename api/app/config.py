import os
import oracledb
from enum import Enum

# Database settings
class DatabaseSettings(Enum):
	DB_DSN = os.environ.get("ORACLE_CLOUD_DSN") or "coleccionista-bd-oracle-test:1521/xe"
	DB_USER = os.environ.get("ORACLE_CLOUD_USER") or "system"
	DB_PASSWORD = os.environ.get("ORACLE_CLOUD_PASSWORD") or "myPassword123"
	MIN_POOL = 2 if os.environ.get("PRODUCTION") == "True" else 1
	MAX_POOL = 5 if os.environ.get("PRODUCTION") == "True" else 1
	POOL_INCREMENT = 1 if os.environ.get("PRODUCTION") == "True" else 0

def init_pool():
	pool = oracledb.create_pool( user=DatabaseSettings.DB_USER.value,
								 password=DatabaseSettings.DB_PASSWORD.value,
								 dsn=DatabaseSettings.DB_DSN.value,
								 min=DatabaseSettings.MIN_POOL.value,
								 max=DatabaseSettings.MAX_POOL.value,
							     increment=DatabaseSettings.POOL_INCREMENT.value)
	return pool

