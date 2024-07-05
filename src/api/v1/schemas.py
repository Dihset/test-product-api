from typing import Any, Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel, Field

TData = TypeVar("TData")
TListItem = TypeVar("TListItem")


class PaginationOut(BaseModel):
    page: int
    limit: int
    total: int


class ListPaginatedResponse(BaseModel, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(BaseModel, Generic[TData]):
    data: TData | dict | list = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)


class ProductOutSchema(BaseModel):
    oid: UUID | None
    name: str
    description: str
    price: int
    category: str
