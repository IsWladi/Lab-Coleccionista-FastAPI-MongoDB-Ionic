# Lab-Coleccionista-FastAPI-Oracle
**This repository is for experimentation only, for the study of the infrastructure and development cycle of the portfolio project for DuocUC.**

# Needed Github Repository Secrets
- As of now, there are no repository secrets for Oracle Database Cloud connections because, until now, a cloud database has not been available

# Notes
- Bug: If I've updated the repository secrets, I need to update the environment variables in Deta Space because they are not updated automatically.
- Check if it's an improvement to replace bcrypt with argon2-cffi.

# Published API ( as of now, only works with MongoDB Atlas):
[Deta Space](https://lab_portafolio-1-k1767315.deta.app/)

# How to Run the Project Locally with Docker
## Requirements
- Docker and Docker Compose
- [SQL Developer 23.1.0](https://www.oracle.com/tools/downloads/sqldev-downloads-23.1.0.html)
- Ionic Framework v7.0.0:  `npm i -g @ionic/cli@7.0.0`

## Run Docker Containers
- Execute `docker compose up -d` at the root of the project (if you encounter an error about the compose command, try with `docker-compose up -d`, as this may occur with older versions of Docker).
- Note: The wait for the command's end may be longer than 5 minutes because it is going to download the Oracle database.

## Connect to the Database via SQL Developer
- Use the example below (the password is defined in the compose.yaml file):
  ![image](https://github.com/IsWladi/Lab-Ionic-FastAPI-MongoDB/assets/133131317/458c3c71-6645-4d8d-a9c4-ec5d70bf7e3b)

# How to manage the containers
- Execute `docker compose stop` at the root of the project to stop the containers.
- Execute `docker compose start` at the root of the project to start the containers.
- Note:
    * If you want to restart the containers, avoid using `docker compose restart` because by default the database is started after the API. Instead, use `docker compose stop` and then `docker compose start`.
    * The API container has hot reload enabled, so you don't need to restart it when you make changes to the code.

# How to run the tests
- When the containers are running, execute `docker exec -it coleccionista-api-test bash` to enter the container.
- Once inside the container:
    - Execute `pytest` to run all the tests.
    - Execute `pytest -k <filename>.py` to run a specific test.
    - To see the verbose output of the tests, add the `-v` or '-vv' flags to the previous commands.


# Documentation:
- [FastAPI web](https://fastapi.tiangolo.com/)
- [Run a Python App on DetaSpace](https://deta.space/docs/en/build/quick-starts/python/)
- [GitHub Action for DetaSpace](https://github.com/marketplace/actions/deta-space-deployment-github-action)
- [Setting Environment Variables within a Spacefile](https://deta.space/docs/en/build/fundamentals/the-space-runtime/configuration#environment-variables)
- [Oracle Container Registry - Oracle Database XE Release 21c (21.3.0.0)](https://container-registry.oracle.com/ords/f?p=113:4:100485902704522:::4:P4_REPOSITORY,AI_REPOSITORY,AI_REPOSITORY_NAME,P4_REPOSITORY_NAME,P4_EULA_ID,P4_BUSINESS_AREA_ID:803,803,Oracle%20Database%20Express%20Edition,Oracle%20Database%20Express%20Edition,1,0&cs=3DDK2EFrARkHzaJP7vopfqmoDgt3IQ9zeD_aMJZhQdYo1nanPtxGMH5iJoA3VS5hyHGzfJtQeX4btShVmbP6vWA)
- [SQL Developer 23.1.0](https://www.oracle.com/tools/downloads/sqldev-downloads-23.1.0.html)
- [python - oracledb documentation](https://python-oracledb.readthedocs.io/en/latest/)
