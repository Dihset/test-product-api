from dataclasses import dataclass

from src.domain.entities import Product


@dataclass
class GetProductCommand:
    oid: str


@dataclass
class CreateProductCommand:
    product: Product


@dataclass
class DeleteProductCommand:
    oid: str
