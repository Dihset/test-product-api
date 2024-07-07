import enum
from dataclasses import dataclass, fields


@dataclass
class Product:
    oid: str | None
    name: str
    description: str
    price: int
    category: str


ProductSortFieldsEnum = enum.Enum(
    "ProductListField",
    {field.name: field.name for field in fields(Product)},
)
