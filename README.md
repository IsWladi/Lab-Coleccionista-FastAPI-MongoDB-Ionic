# Lab-Coleccionista-FastAPI-Oracle
**This repository is for experimentation only, for the study of the infrastructure and development cycle of the portfolio project for DuocUC.**

## Table of contents
* [Notes](#notes)
* [Published API](#published-api)
* [How to publish the API to DetaSpace](#how-to-publish-the-api-to-detaspace)
    * [Needed GitHub Repository Secrets](#needed-github-repository-secrets)
    * [Publish the API](#publish-the-api)
* [How to Run the Project Locally with Docker](#how-to-run-the-project-locally-with-docker)
    * [Requirements](#requirements)
    * [Run Docker Containers](#run-docker-containers)
    * [Connect to the Database via SQL Developer](#connect-to-the-database-via-sql-developer)
* [How to manage the containers](#how-to-manage-the-containers)
* [How to run the tests](#how-to-run-the-tests)
* [Project Structure](#project-structure)
* [References](#references)

# Notes
- Bug: If I've updated the repository secrets, I need to update the environment variables in Deta Space because they are not updated automatically.
- Check if it's an improvement to replace bcrypt with argon2-cffi.

# Published API
( as of now, there is no published API until I have an Oracle cloud database )

# How to publish the API to DetaSpace
## Needed Github Repository Secrets
- As of now, there are no repository secrets for Oracle Database Cloud connections because, until now, a cloud database has not been available

## Publish the API
- Make a pull request to the `main` branch:
    - The GitHub Action will run the tests for being able to merge the pull request.
    - When merged, the GitHub Action will publish the API to Deta Space.

# How to Run the Project Locally with Docker
## Requirements
- Docker and Docker Compose
- [SQL Developer 23.1.0](https://www.oracle.com/tools/downloads/sqldev-downloads-23.1.0.html)

## Run Docker Containers
- Execute `docker compose up -d` at the root of the project (if you encounter an error about the compose command, try with `docker-compose up -d`, as this may occur with older versions of Docker).
- When finished, navegate to `localhost:8000/docs` to view the api documentation
- Note: The wait time for the command to complete may exceed 5 minutes as it involves downloading the Oracle database. Additionally, the API container will wait until the database is in a healthy state before receiving connections, ensuring that the API functions correctly.

## Connect to the Database via SQL Developer
- Use the example below (the password is defined in the compose.yaml file):
  ![image](https://github.com/IsWladi/Lab-Ionic-FastAPI-MongoDB/assets/133131317/458c3c71-6645-4d8d-a9c4-ec5d70bf7e3b)

# How to manage the containers
- Execute `docker compose start` at the root of the project to start the containers.
- Execute `docker compose stop` at the root of the project to stop the containers.
- Note:
    * If you want to restart the containers, avoid using `docker compose restart` because a bug cause that the database is started after the API. Instead, use `docker compose stop` and then `docker compose start`.
    * The API container has hot reload enabled, so you don't need to restart it when you make changes to the code.

# How to run the tests
- When the containers are running, execute `docker exec -it coleccionista-api-test bash` to enter the container.
- Once inside the container:
    - Execute `pytest` to run all the tests.
    - Execute `pytest -k <filename>.py` to run a specific test.
    - To see the verbose output of the tests, add the `-v` or `-vv` flags to the previous commands.

# Project Structure

## Route: `./`
- `.github/` - GitHub Actions workflows (CI/CD)
- `api/` - API configuration files and source code
- `.dockerignore` - Files to ignore when building the Docker images
- `.gitignore` - Files to ignore when pushing to the repository
- `.spaceignore` - Files to ignore when deploying to Deta Space
-  `README.md` - Documentation of the project
- `Spacefile` - Deta Space configuration file (for deployment)
- `compose.yaml` - Docker Compose configuration file for local development (FastAPI + Oracle DB)

## Route: `./api/`
- `app/` - API source code (FastAPI)
- `Dockerfile` - Docker configuration file for the FastAPI app
- `requirements.txt` - Python dependencies for the FastAPI app

## Route: `./api/app/`
- `models/` - Pydantic models for be used in the endpoints
- `routers/` - API source code for each set of endpoints ( for separation of concerns)
- `tests/` - API tests (pytest)
- `config.py` - Environment variables, database connection function, secrets, etc.
- `dependencies.py` - Dependency injection for the endpoints
- `main.py` - API main file ( app creation, routers addition, definition of the lifespan events, etc. )

# References:

## API
- [API - Project Documentation](./api/app/README.md)
- [FastAPI - web](https://fastapi.tiangolo.com/)
- [FastAPI - How to mantain global pool connections](https://github.com/tiangolo/fastapi/issues/1800)
- [FastAPI - Lifespan Events](https://fastapi.tiangolo.com/advanced/events/)
- [FastAPI - Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)
- [FastAPI - OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [FastAPI - Testing](https://fastapi.tiangolo.com/tutorial/testing/)

## Database
- [Oracle - Oracle Container Registry - Oracle Database XE Release 21c (21.3.0.0)](https://container-registry.oracle.com/ords/f?p=113:4:8227059033940:::4:P4_REPOSITORY,AI_REPOSITORY,AI_REPOSITORY_NAME,P4_REPOSITORY_NAME,P4_EULA_ID,P4_BUSINESS_AREA_ID:803,803,Oracle%20Database%20Express%20Edition,Oracle%20Database%20Express%20Edition,1,0&cs=3UHW8565qyh-pcnTW8hJpndMMN-pfSM4R7K2Ym0DrVdyu1QIujgszQIXdX2SJ9sbj4tBMXfJtH9oqtBh917cpfw)
- [Oracle - SQL Developer 23.1.0](https://www.oracle.com/tools/downloads/sqldev-downloads-23.1.0.html)
- [Python/Oracle - oracledb documentation](https://python-oracledb.readthedocs.io/en/latest/)

## Deployment
- [DetaSpace - Run a Python App on DetaSpace](https://deta.space/docs/en/build/quick-starts/python/)
- [DetaSpace - GitHub Action for DetaSpace](https://github.com/marketplace/actions/deta-space-deployment-github-action)
- [DetaSpace - Setting Environment Variables within a Spacefile](https://deta.space/docs/en/build/fundamentals/the-space-runtime/configuration#environment-variables)

## Docker
- [DockerHub - Python](https://hub.docker.com/_/python)
- [Docker Compose - Healthcheck](https://docs.docker.com/compose/compose-file/compose-file-v3/#healthcheck)
- [Docker Compose - Depends on (with or whitout condition)](https://docs.docker.com/compose/compose-file/05-services/#depends_on)
