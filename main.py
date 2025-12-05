# main.py
from fastapi import FastAPI
from product_routes import app as product_router

app = FastAPI(
    title="E-Commerce Product API",
    description="A simple API for managing e-commerce products",
    version="1.0.0"
)

# Include product routes
app.include_router(product_router, prefix="/api")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the E-Commerce Product API"}

