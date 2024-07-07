import enum
from dataclasses import dataclass, field

from src.domain.entities import Product


@dataclass
class PaginationQuery:
    page: int = 0
    limit: int = 10

    @property
    def offset(self):
        return self.page * self.limit


class SortOrderEnum(int, enum.Enum):
    asc = 1
    decs = -1


@dataclass
class ProductSortQuery:
    field: str = "id"
    order: SortOrderEnum = SortOrderEnum.asc


@dataclass
class GetProductListCommand:
    search: str
    pagination: PaginationQuery = field(default_factory=PaginationQuery)
    sort: ProductSortQuery = field(default_factory=ProductSortQuery)


@dataclass
class GetProductCommand:
    oid: str


@dataclass
class CreateProductCommand:
    product: Product


@dataclass
class UpdateProductCommand:
    product: Product


@dataclass
class DeleteProductCommand:
    oid: str
