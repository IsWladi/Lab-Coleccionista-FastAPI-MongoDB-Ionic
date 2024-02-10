from fastapi.testclient import TestClient

from app.main import app

def test_get_all_users_without_authentication():
    client = TestClient(app)
    response = client.get("api/examples/get/all/users/without/authentication")
    assert response.status_code == 200
