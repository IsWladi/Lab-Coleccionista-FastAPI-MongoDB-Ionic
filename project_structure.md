# main file structure of the project: ./
  .github/ - GitHub Actions workflows (CI/CD)
  api/ - API configuration files and source code
󰡨  .dockerignore - Files to ignore when building the Docker image
  .gitignore - Files to ignore when pushing to the repository
  .spaceignore - Files to ignore when deploying to Deta Space
  README.md
  Spacefile - Deta Space configuration file
󰡨  compose.yaml - Docker Compose configuration file

# API configuration file and soure code: ./api/
  app/ - API source code (FastAPI)
󰡨  Dockerfile - Docker configuration file for the FastAPI app
󰈙  requirements.txt - Python dependencies for the FastAPI app

# API source code: ./api/app/
  models/ - Pydantic models for be used in the endpoints
  routers/ - API source code for each set of endpoints ( for separation of concerns)
  tests/ - API tests (pytest)
  __init__.py
  config.py - Oracle database configuration
  main.py - API main file

