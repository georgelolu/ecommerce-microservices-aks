from fastapi import FastAPI, HTTPException

app = FastAPI(title="E-Commerce Inventory Service", version="1.0.0")

STOCK = {
    1: {"product_id": 1, "available": 25},
    2: {"product_id": 2, "available": 15},
    3: {"product_id": 3, "available": 40},
}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "inventory"}


@app.get("/inventory/{product_id}")
def get_inventory(product_id: int):
    if product_id not in STOCK:
        raise HTTPException(status_code=404, detail="Product not found")

    return STOCK[product_id]
