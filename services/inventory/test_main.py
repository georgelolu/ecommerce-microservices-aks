from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "inventory"


def test_get_existing_inventory():
    response = client.get("/inventory/1")
    assert response.status_code == 200
    assert response.json() == {"product_id": 1, "available": 25}


def test_missing_inventory_returns_404():
    response = client.get("/inventory/999")
    assert response.status_code == 404
