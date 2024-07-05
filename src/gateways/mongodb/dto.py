from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from uuid import uuid4

from src.domain.entities import Product


class BaseDto(ABC):
    def dump(self):
        return asdict(self)

    @staticmethod
    @abstractmethod
    def load(data: dict) -> "BaseDto":
        pass


@dataclass
class ProductDto(BaseDto):
    oid: str | None
    name: str
    description: str
    price: int
    category: str

    def __post_init__(self):
        if not self.oid:
            self.oid = str(uuid4())

    @staticmethod
    def load(data: dict) -> "ProductDto":
        return ProductDto(
            oid=data.get("oid"),
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            category=data.get("category"),
        )

    @staticmethod
    def from_entity(entity: Product) -> "ProductDto":
        return ProductDto(
            oid=entity.oid,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            category=entity.category,
        )

    def to_entity(self) -> Product:
        return Product(
            oid=self.oid,
            name=self.name,
            description=self.description,
            price=self.price,
            category=self.category,
        )
