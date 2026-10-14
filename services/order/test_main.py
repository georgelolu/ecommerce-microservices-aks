from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "order"


def test_create_and_retrieve_order():
    response = client.post(
        "/orders",
        json={"product_id": 1, "quantity": 2},
    )
    assert response.status_code == 201

    order = response.json()
    assert order["product_id"] == 1
    assert order["quantity"] == 2
    assert order["status"] == "created"

    retrieved = client.get(f"/orders/{order['order_id']}")
    assert retrieved.status_code == 200
    assert retrieved.json() == order


def test_zero_quantity_is_rejected():
    response = client.post(
        "/orders",
        json={"product_id": 1, "quantity": 0},
    )
    assert response.status_code == 422


def test_missing_order_returns_404():
    response = client.get("/orders/nonexistent-order")
    assert response.status_code == 404
