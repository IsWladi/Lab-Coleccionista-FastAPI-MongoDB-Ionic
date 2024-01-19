# API documentation

## How oauth2 works in this app

### File `api\app\routers\auth.py`:
 * Use the standard OAuth2 protocol documented and adapted for FastAPI.
 * The `/api/auth/token` endpoint is defined.
     * It is used to validate the login and return a token if it is correct, to be used in subsequent requests.
     * The token that is returned is a JSON Web Token (JWT).
     * The token has an expiration time.
     * The token is signed with a secret key (whitout the secret key, the token can´t be decoded).
     * The token is encoded with the HS256 algorithm.
     * OAuth2 was designed so that the backend or API could be independent of the server that authenticates the user.
         * But in this case, the same FastAPI application will handle the API and the authentication.
 * The endpoint has to be called with form data, with the following fields:
     * `username`: The username of the user to authenticate.
     * `password`: The password of the user to authenticate.
 * The frontend will send the form data to the endpoint and will receive the token.

### File `api\app\dependencies.py`:
 * The function `get_current_user` is defined:
     * It is a dependency that will be used in other endpoints.
     * If a endpoint depends on this function, it will be validate the authentication of the user.
     * It will receive the bearer token.
     * It will verify that the token is valid.
     * It will return the current user.
     * If the token is invalid, it will return an error.

### How to make an endpoint that requires authentication:
 * Import the following in the endpoint file:
   ```python
      from fastapi import Depends
      from app.dependencies import get_current_user
      from typing import Annotated
      from app.models.basic_auth_models import User
    ```
 * Define in a variable the dependency:
    ```python
       auth_dependency = Annotated[User, Depends(get_current_user)] # for use: current_user: auth_dependency
    ```
 * Use the variable in the endpoint parameter, example:
    ```python
       @router.get("/get/item/{item}", status_code=200)
       async def get_item_by_id(item: str, current_user: auth_dependency):
    ```
 * The endpoint will only be executed if the token is valid.
