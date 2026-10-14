from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import uuid4

app = FastAPI(title="E-Commerce Order Service", version="1.0.0")

ORDERS = {}


class OrderRequest(BaseModel):
    product_id: int
    quantity: int = Field(gt=0, le=100)


@app.get("/health")
def health():
    return {"status": "healthy", "service": "order"}


@app.post("/orders", status_code=201)
def create_order(order: OrderRequest):
    order_id = str(uuid4())

    record = {
        "order_id": order_id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "status": "created",
    }

    ORDERS[order_id] = record
    return record


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    if order_id not in ORDERS:
        raise HTTPException(status_code=404, detail="Order not found")

    return ORDERS[order_id]
