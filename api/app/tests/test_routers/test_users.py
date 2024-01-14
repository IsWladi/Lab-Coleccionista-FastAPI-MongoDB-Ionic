from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_valid_user():
    response = client.get("/api/users/get/user1")
    assert response.status_code == 200
    assert response.json() == {"username": "user1"}

def test_get_unexisting_user():
	response = client.get("/api/users/get/fakeuser")
	assert response.status_code == 404
	assert response.json() == {"detail": "User not found"}
