from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

from src.domain.entities import Product

TData = TypeVar("TData")
TListItem = TypeVar("TListItem")


class PaginationOutSchema(BaseModel):
    page: int
    limit: int
    total: int


class ListPaginatedResponse(BaseModel, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOutSchema


class ApiResponse(BaseModel, Generic[TData]):
    data: TData | dict | list = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)


class ProductOutSchema(BaseModel):
    oid: str
    name: str
    description: str
    price: int
    category: str

    @staticmethod
    def from_entity(entity: Product) -> "ProductOutSchema":
        return ProductOutSchema(
            oid=entity.oid,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            category=entity.category,
        )


class ProductInSchema(BaseModel):
    name: str
    description: str
    price: int
    category: str

    def to_entity(self, oid: str | None = None) -> Product:
        return Product(
            oid=oid,
            name=self.name,
            description=self.description,
            price=self.price,
            category=self.category,
        )
