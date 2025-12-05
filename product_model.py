class Product:
    def __init__(self, id: int, name: str, description: str, price: float, category: str, in_stock: int, id_active: bool, tag: str = None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.in_stock = in_stock
        self.id_active = id_active
        self.tag = tag

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "in_stock": self.in_stock,
            "id_active": self.id_active,
            "tag": self.tag,
        }