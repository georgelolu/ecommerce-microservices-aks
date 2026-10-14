from fastapi import FastAPI

app = FastAPI(title="E-Commerce Product Service", version="1.0.0")

PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 59.99},
    {"id": 2, "name": "Smart Watch", "price": 89.99},
    {"id": 3, "name": "Laptop Stand", "price": 29.99},
]


@app.get("/health")
def health():
    return {"status": "healthy", "service": "product"}


@app.get("/products")
def get_products():
    return {"items": PRODUCTS, "count": len(PRODUCTS)}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}
