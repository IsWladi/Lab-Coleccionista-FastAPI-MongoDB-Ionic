# Project Structure explanation

## Route: `./`
- `.github/ -` GitHub Actions workflows (CI/CD)
- `api/ -` API configuration files and source code
- `.dockerignore -` Files to ignore when building the Docker images
- `.gitignore -` Files to ignore when pushing to the repository
- `.spaceignore -` Files to ignore when deploying to Deta Space
-  `README.md` - Documentation of the project
- `Spacefile -` Deta Space configuration file (for deployment)
- `compose.yaml -` Docker Compose configuration file for local development (FastAPI + Oracle DB)

## Route: `./api/`
- `app/ -` API source code (FastAPI)
- `Dockerfile -` Docker configuration file for the FastAPI app
- `requirements.txt -` Python dependencies for the FastAPI app

## Route: `./api/app/`
- `models/ -` Pydantic models for be used in the endpoints
- `routers/ -` API source code for each set of endpoints ( for separation of concerns)
- `tests/ -` API tests (pytest)
- `config.py -` Oracle database configuration
- `main.py -` API main file

