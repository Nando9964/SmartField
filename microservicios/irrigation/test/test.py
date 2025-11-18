import pytest
from app.irrigation import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_activate_irrigation(client):
    response = client.post('/activate-irrigation', json={"crop_type": "tomato"})
    assert response.status_code == 200
    assert 'Riego activado' in response.json.get('message')
