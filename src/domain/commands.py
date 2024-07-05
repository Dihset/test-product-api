from dataclasses import dataclass

from src.domain.entities import Product


@dataclass
class CreateProductCommand:
    product: Product
