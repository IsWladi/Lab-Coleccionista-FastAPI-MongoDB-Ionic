from fastapi.testclient import TestClient

from app.main import app

# When a endpoint has a db connection, is required to use the "with" statement(this makes sure the db pool is available)
# docs: https://fastapi.tiangolo.com/advanced/testing-events/#testing-events-startup-shutdown
def test_get_valid_user():
    with TestClient(app) as client:
        response = client.get("/api/users/get/user1")
        assert response.status_code == 200
        assert response.json() == {"username": "user1"}

def test_get_unexisting_user():
    with TestClient(app) as client:
        response = client.get("/api/users/get/fakeuser")
        assert response.status_code == 404
        assert response.json() == {"detail": "User not found"}
