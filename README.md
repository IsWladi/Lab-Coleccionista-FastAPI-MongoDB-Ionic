# documentation:
- [Run a python app on DetaSpace](https://deta.space/docs/en/build/quick-starts/python/)
- [GitHub Action for Deta](https://github.com/marketplace/actions/deta-space-deployment-github-action)
- [Setting environment variables](https://deta.space/docs/en/build/fundamentals/the-space-runtime/configuration#environment-variables)
- [Oracle container registry - Oracle Database XE Release 21c (21.3.0.0) ](https://container-registry.oracle.com/ords/f?p=113:4:100485902704522:::4:P4_REPOSITORY,AI_REPOSITORY,AI_REPOSITORY_NAME,P4_REPOSITORY_NAME,P4_EULA_ID,P4_BUSINESS_AREA_ID:803,803,Oracle%20Database%20Express%20Edition,Oracle%20Database%20Express%20Edition,1,0&cs=3DDK2EFrARkHzaJP7vopfqmoDgt3IQ9zeD_aMJZhQdYo1nanPtxGMH5iJoA3VS5hyHGzfJtQeX4btShVmbP6vWA)

# Notes:
- Check if it's necessary to replace bcrypt with argon2-cffi.

# Github Repository Secrets
- ACCESS_TOKEN: `deta access token`
- PROJECT_ID: `deta project id`
- MONGO_USERNAME: `mongo username`
- MONGO_PASSWORD: `mongo password`
- MONGO_CLUSTER: `mongo cluster`

# Notes
- Bug: If I´ve updated the repository secrets, I need to update the environment variables in the Deta Space because they are not updated automatically.

# Published API:
[Deta Space](https://lab_portafolio-1-k1767315.deta.app/)

# How to run the project locally
## Requirements
- Docker and Docker Compose
- Sqldeveloper 23.1
- Ionic Framework v7.0.0

