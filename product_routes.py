from fastapi import APIRouter, HTTPException
from typing import List
from product_schema import ProductCreate, ProductUpdate
from product_model import Product 

app = APIRouter()

products_db: List[Product] = []

next = 1

@app.post("/products", response_model=ProductCreate)
def create_product(product: ProductCreate):
    global next
    new_product = Product(
        id=next,
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        in_stock=product.in_stock,
        id_active=product.id_active,
        tag=product.tag
    )
    products_db.append(new_product)
    next += 1
    return new_product.to_dict()

#read All products
@app.get("/products", response_model=List[ProductCreate])
def get_products():
    return [prod.to_dict() for prod in products_db]

#read product by id
@app.get("/products/{product_id}", response_model=ProductCreate)
def get_product(product_id: int):
    for prod in products_db:
        if prod.id == product_id:
            return prod.to_dict()
    raise HTTPException(status_code=404, detail="Product not found")

#update product by id
@app.put("/products/{product_id}", response_model=ProductCreate)
def update_product(product_id: int, updated_product: ProductUpdate):
    for prod in products_db:
        if prod.id == product_id:
            prod.name = updated_product.name
            prod.description = updated_product.description
            prod.price = updated_product.price
            prod.category = updated_product.category
            prod.in_stock = updated_product.in_stock
            prod.id_active = updated_product.id_active
            prod.tag = updated_product.tag
            return prod.to_dict()
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, prod in enumerate(products_db):
        if prod.id == product_id:
            products_db.pop(index)
            return {"detail": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")