from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_available_cars_success():

    response = client.get("/available_cars", params={"date1": "2025-01-15"})
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["id"] == "AA111AA"
    assert response.json()[1]["id"] == "BB222BB"
    assert response.json()[2]["id"] == "CC333CC"

def test_get_available_cars_no_cars():

    response = client.get("available_cars", params={"date1": "2025-01-26"})
    assert response.status_code == 200
    assert response.json() == []

def test_get_available_cars_invalid_date():

    response = client.get("available_cars", params={"date1": "15-01-2025"})
    assert response.status_code == 422