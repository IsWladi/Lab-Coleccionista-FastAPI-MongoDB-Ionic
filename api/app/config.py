import os
import oracledb

def get_database_cursor():
	# if $PRODUCTION == "True" conect to oracle cloud, else connect to local database within docker container
	if os.environ.get("PRODUCTION") == "True":
		# Connect to Oracle Cloud
		return {error: "Not implemented yet"}

	else:
		# Connect to local database within docker container
		local_password = "myPassword123"

		connection = oracledb.connect(
			user="system",
			password=local_password,
			dsn="coleccionista-bd-oracle-test:1521/xe")

		print("Successfully connected to Oracle Database")

		cursor = connection.cursor()

		# Create a table for users if it doesn't exist

		# cursor.execute("""
		# 	DECLARE
		# 	  table_exists INTEGER;
		# 	BEGIN
		# 	  SELECT COUNT(*)
		# 	  INTO table_exists
		# 	  FROM user_tables
		# 	  WHERE table_name = 'USERS';
		#
		# 	  IF table_exists = 0 THEN
		# 		EXECUTE IMMEDIATE 'CREATE TABLE users (
		# 		  username VARCHAR2(20),
		# 		  password VARCHAR2(4000),
		# 		  PRIMARY KEY (username)
		# 		)';
		# 	  END IF;
		# 	END;""")

		return cursor

