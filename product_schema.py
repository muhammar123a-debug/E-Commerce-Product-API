from pydantic import BaseModel
from typing import Optional

# Naya product create karne ke liye
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    in_stock: int
    id_active: bool
    tag: Optional[str] = None

# Product update karne ke liye (sari fields optional)
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    in_stock: Optional[int] = None
    id_active: Optional[bool] = None
    tag: Optional[str] = None
