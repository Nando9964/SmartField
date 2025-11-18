import pytest
from app.monitoring import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_monitor_data(client):
    response = client.post('/monitor', json={"crop_type": "tomato"})
    assert response.status_code == 200
    assert 'temperature' in response.json
    assert 'humidity' in response.json
    assert 'nutrient_level' in response.json
