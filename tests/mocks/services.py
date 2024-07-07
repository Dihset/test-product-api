from uuid import uuid4

from src.domain.entities import Product
from src.domain.services import IProductService
from tests.mocks.factories import ProductFactory


class DummyProductService(IProductService):
    async def get_by_id(self, oid: str) -> Product:
        return ProductFactory.build(oid=oid)

    async def create(self, product: Product) -> Product:
        product.oid = str(uuid4())
        return product

    async def update(self, product: Product) -> Product:
        return product

    async def delete(self, oid: str) -> Product:
        return ProductFactory.build(oid=oid)

    async def find_many(
        self,
        sort_field: str,
        sort_order: int,
        offset: int,
        limit: int,
        search: str | None = None,
    ) -> list[Product]:
        pass

    async def count_many(self, search: str | None = None) -> int:
        pass
