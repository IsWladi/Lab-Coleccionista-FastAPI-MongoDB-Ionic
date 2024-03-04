# Lab-Coleccionista-FastAPI-MongoDB-Ionic
**This repository is for experimentation only, for the study of the infrastructure and development cycle of the portfolio project for DuocUC.**

## Table of contents
- [Notes](#notes)
- [Published API](#published-api)
- [How to publish the API to DetaSpace](#how-to-publish-the-api-to-detaspace)
  * [Needed Github Repository Secrets](#needed-github-repository-secrets)
  * [Publish the API](#publish-the-api)
- [How to set up the local environment](#how-to-set-up-the-local-environment)
  * [Set Up FastAPI and MongoDB with Docker](#set-up-fastapi-and-mongodb-with-docker)
    + [Requirements](#requirements)
    + [Run Docker Containers](#run-docker-containers)
    + [Connect to the Database via MongoDB Compass](#connect-to-the-database-via-mongodb-compass)
  * [Set Up the Ionic APP Locally](#set-up-the-ionic-app-locally)
    + [Requirements](#requirements-1)
    + [Running the App](#running-the-app)
- [How to Manage the Environment](#how-to-manage-the-environment)
  * [Manage the containers (basic usage) - FastAPI and MongoDB](#manage-the-containers-(basic-usage)---fastapi-and-mongodb)
  * [Run the tests - FastAPI](#run-the-tests---fastapi)
- [Project Structure](#project-structure)
- [References:](#references)
  * [API](#api)
  * [Database](#database)
  * [Deployment](#deployment)
  * [Continuous Integration/Continuous Deployment](#continuous-integrationcontinuous-deployment)
  * [Docker](#docker)

# Notes
- Bug: If I've updated the repository secrets, I need to update the environment variables in Deta Space because they are not updated automatically.

# Published API
[Deta Space](https://lab_portafolio-1-k1767315.deta.app/)

# How to publish the API to DetaSpace
## Needed Github Repository Secrets
- ACCESS_TOKEN: `deta access token`
- PROJECT_ID: `deta project id`
- MONGO_USERNAME: `mongo username`
- MONGO_PASSWORD: `mongo password`
- MONGO_CLUSTER: `mongo cluster`

## Publish the API
- Make a pull request to the `main` branch:
    - The GitHub Action will run the tests for being able to merge the pull request.
    - When merged, the GitHub Action will publish the API to Deta Space.

# How to set up the local environment

## Set Up FastAPI and MongoDB with Docker

### Requirements
- Linux:
    - [Docker engine (with docker compose)](https://docs.docker.com/engine/install/)
- Windows:
    - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    - Manage docker in wsl2 distro terminal (Optional but recommended because it's faster and enable hot reload):
        * After installing Docker Desktop, install a Linux distro with WSL2: [Tutorial](https://terminaldelinux.com/terminal/wsl/instalacion-wsl/)
        * Enable Docker support in your WSL 2 distro: [Tutorial](https://docs.docker.com/desktop/wsl/#enabling-docker-support-in-wsl-2-distros)
        * (optional) configure the WSL2 for comfortable development:
            * [Set up WSL2](https://terminaldelinux.com/terminal/wsl/configuracion-wsl/)
            * [Install zsh in WSL2 distro](https://terminaldelinux.com/terminal/preparacion-entorno/instalacion-zsh/)
        * Notes:
            * Clone the repository in the wsl2 distro filesystem, not in Windows filesystem.
            * You can manage the containers in Windows by referring to the WSL2 distro's filesystem..
            * If you don´t want to edit the files in the WSL2 distro, you can edit them in Windows([access Linux from Windows](https://terminaldelinux.com/terminal/wsl/configuracion-wsl/#acceder-a-linux-desde-windows)) and the changes will be reflected in the WSL2 distro filesystem.

- [MongoDB Compass](https://www.mongodb.com/try/download/compass)

### Run Docker Containers
- Execute `docker compose up -d` at the root of the project (if you encounter an error about the compose command, try with `docker-compose up -d`, as this may occur with older versions of Docker).
- When finished, navegate to `localhost:8000/docs` to view the api documentation

### Connect to the Database via MongoDB Compass
- Use the example below (the username and password are defined in the compose.yaml file):
   ![image](https://github.com/IsWladi/Lab-Portfolio-Ionic-FastAPI-Oracle/assets/133131317/15f15744-4a90-4ef0-ab4b-94ff0724d121)


## Set Up the Ionic APP Locally

### Requirements
- [Node v20.11.1](https://nodejs.org/en)
- Ionic 7.1.1: `npm install -g @ionic/cli@7.1.1`
- Angular 17.1.1: `npm install -g @angular/cli@17.1.1`
- Android Studio

### Running the App
- [Ensure that the FastAPI and MongoDB containers are running.](#manage-the-containers-(basic-usage)---fastapi-and-mongodb)
- Open your terminal and navigate to the ./mobile/coleccti-mate/ folder.
- Execute the command: `ionic serve`
- Optional: To test the app with the production configuration (which accesses the DetaSpace API instead of the local API), use: `ionic serve --prod`
- When finished, navegate to `localhost:8100/` to view the Ionic app.

# How to Manage the Environment

## Manage the containers (basic usage) - FastAPI and MongoDB
- Execute `docker compose start` at the root of the project to start the containers.
- Execute `docker compose stop` at the root of the project to stop the containers.
- Note:
    * The API container have hot reload enabled, so you don't need to restart the containers when you make changes to the code.

## Run the tests - FastAPI
- When the containers are running, execute `docker exec -it coleccionista-api-test bash` to enter the container.
- Once inside the container:
    - Execute `pytest` to run all the tests.
    - Execute `pytest -k <filename>.py` to run a specific test.
    - To see the verbose output of the tests, add the `-v` or `-vv` flags to the previous commands.

# Project Structure

## Route: `./`
- `.github/` - GitHub Actions workflows (CI/CD)
- `api/` - API configuration files and source code
- `mobile/` - Ionic app configuration files and source code
- `.dockerignore` - Files to ignore when building the Docker images
- `.gitignore` - Files to ignore when pushing to the repository
- `.spaceignore` - Files to ignore when deploying to Deta Space
-  `README.md` - Documentation of the project
- `Spacefile` - Deta Space configuration file (for deployment)
- `compose.yaml` - Docker Compose configuration file for local development

## Route: `./api/`
- `app/` - API source code (FastAPI)
- `Dockerfile` - Docker configuration file for the FastAPI app
- `requirements.txt` - Python dependencies for the FastAPI app

## Route: `./api/app/`
- `dependencies/` - Avaliable dependencies for the API (db, auth, etc.)
- `models/` - Pydantic models for be used in the endpoints
- `routers/` - API source code for each set of endpoints ( for separation of concerns)
- `tests/` - API tests (pytest)
- `README.md` - Specific documentation for the API (not as a replacement for the Swagger docs)
- `main.py` - API main file ( app creation, routers addition, definition of the lifespan events, etc. )
- `settings.py` - Enums; environment variables, secrets, etc.

## Route: `./mobile/`
- `./coleccti-mate/` - APP source code (Ionic)
- `Dockerfile` - Docker configuration file for the Ionic app

# References:

## API
- [API - Project Documentation](./api/app/README.md)
- [FastAPI - web](https://fastapi.tiangolo.com/)
- [FastAPI - How to mantain global pool connections](https://github.com/tiangolo/fastapi/issues/1800)
- [FastAPI - Lifespan Events](https://fastapi.tiangolo.com/advanced/events/)
- [FastAPI - Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)
- [FastAPI - OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [FastAPI - Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [FastAPI - Advanced testing, lifespan](https://fastapi.tiangolo.com/advanced/testing-events/#testing-events-startup-shutdown)

## Database
- [MongoDB Web](https://www.mongodb.com/)
- [MongoDB Compass](https://www.mongodb.com/products/tools/compass)
- [DockerHub - MongoDB](https://hub.docker.com/_/mongo)
- [Python/MongoDB - PyMongo documentation](https://pymongo.readthedocs.io/en/stable/)

## Deployment
- [DetaSpace - Run a Python App on DetaSpace](https://deta.space/docs/en/build/quick-starts/python/)
- [DetaSpace - GitHub Action for DetaSpace](https://github.com/marketplace/actions/deta-space-deployment-github-action)
- [DetaSpace - Setting Environment Variables within a Spacefile](https://deta.space/docs/en/build/fundamentals/the-space-runtime/configuration#environment-variables)

## Continuous Integration/Continuous Deployment
- [GitHub Actions - Pull request syncronyze](https://github.com/orgs/community/discussions/24567)

## Docker
- [DockerHub - Python](https://hub.docker.com/_/python)
- [Docker Compose - Healthcheck](https://docs.docker.com/compose/compose-file/compose-file-v3/#healthcheck)
- [Docker Compose - Depends on (with or whitout condition)](https://docs.docker.com/compose/compose-file/05-services/#depends_on)
- [Install WSL2 ](https://terminaldelinux.com/terminal/wsl/instalacion-wsl/)
- [Set up WSL2 ](https://terminaldelinux.com/terminal/wsl/configuracion-wsl/)
- [Install zsh in WSL2 distro](https://terminaldelinux.com/terminal/preparacion-entorno/instalacion-zsh/)
- [Docker Desktop - Enable WSL2 ](https://docs.docker.com/desktop/wsl/)
- [Enabling Docker support in WSL2 distros](https://docs.docker.com/desktop/wsl/#enabling-docker-support-in-wsl-2-distros)
