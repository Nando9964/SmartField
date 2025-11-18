import pytest
from app.auth import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login(client):
    response = client.post('/login', json={"username": "test", "password": "password"})
    assert response.status_code == 200
    assert 'access_token' in response.json
