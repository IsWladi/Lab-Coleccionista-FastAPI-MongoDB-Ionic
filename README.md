# documentation:
- [Run a Python App on DetaSpace](https://deta.space/docs/en/build/quick-starts/python/)
- [GitHub Action for DetaSpace](https://github.com/marketplace/actions/deta-space-deployment-github-action)
- [Setting Environment Variables](https://deta.space/docs/en/build/fundamentals/the-space-runtime/configuration#environment-variables)
- [Oracle Container Registry - Oracle Database XE Release 21c (21.3.0.0)](https://container-registry.oracle.com/ords/f?p=113:4:100485902704522:::4:P4_REPOSITORY,AI_REPOSITORY,AI_REPOSITORY_NAME,P4_REPOSITORY_NAME,P4_EULA_ID,P4_BUSINESS_AREA_ID:803,803,Oracle%20Database%20Express%20Edition,Oracle%20Database%20Express%20Edition,1,0&cs=3DDK2EFrARkHzaJP7vopfqmoDgt3IQ9zeD_aMJZhQdYo1nanPtxGMH5iJoA3VS5hyHGzfJtQeX4btShVmbP6vWA)
- [SQL Developer 23.1.0](https://www.oracle.com/tools/downloads/sqldev-downloads-23.1.0.html)

# Github Repository Secrets
- ACCESS_TOKEN: `deta access token`
- PROJECT_ID: `deta project id`
- MONGO_USERNAME: `mongo username`
- MONGO_PASSWORD: `mongo password`
- MONGO_CLUSTER: `mongo cluster`

# Notes
- Bug: If I've updated the repository secrets, I need to update the environment variables in Deta Space because they are not updated automatically.
- Check if it's an improvement to replace bcrypt with argon2-cffi.

# Published API:
[Deta Space](https://lab_portafolio-1-k1767315.deta.app/)

# How to Run the Project Locally with Docker
## Requirements
- Docker and Docker Compose
- [SQL Developer 23.1.0](https://www.oracle.com/tools/downloads/sqldev-downloads-23.1.0.html)
- Ionic Framework v7.0.0:  `npm i -g @ionic/cli@7.0.0`

## Run Docker Containers
- Execute docker compose up -d at the root of the project (if you encounter an error about the compose command, try with docker-compose up -d, as this may occur with older versions of Docker).

## Connect to the Database via SQL Developer
- Use the example below (the password is defined in the compose.yaml file):
  ![image](https://github.com/IsWladi/Lab-Ionic-FastAPI-MongoDB/assets/133131317/458c3c71-6645-4d8d-a9c4-ec5d70bf7e3b)


