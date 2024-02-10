import os
from enum import Enum

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
