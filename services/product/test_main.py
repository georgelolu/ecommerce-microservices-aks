from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "product"


def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json()["count"] == 3
    assert len(response.json()["items"]) == 3


def test_get_existing_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Wireless Headphones"


def test_missing_product_returns_404():
    response = client.get("/products/999")
    assert response.status_code == 404
