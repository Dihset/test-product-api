from dataclasses import dataclass


@dataclass
class Product:
    oid: str | None
    name: str
    description: str
    price: int
    category: str
