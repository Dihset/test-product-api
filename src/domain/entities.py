from dataclasses import dataclass
from uuid import UUID


@dataclass
class Product:
    oid: UUID | None
    name: str
    description: str
    price: int
    category: str
