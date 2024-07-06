from dataclasses import dataclass

from src.domain.entities import Product
from src.domain.errors import ProductNotFoundException
from src.domain.services import IProductService
from src.gateways.mongodb.dto import ProductDto
from src.gateways.mongodb.repositories import IProductRepository
from src.helpers.errors import fail


@dataclass
class MongoProductService(IProductService):
    repository: IProductRepository

    async def get_by_id(self, oid: str) -> Product:
        dto = await self.repository.get_by_id(oid) or fail(ProductNotFoundException())
        return dto.to_entity()

    async def create(self, product: Product) -> Product:
        dto = ProductDto.from_entity(product)
        dto = await self.repository.create(dto)
        return dto.to_entity()

    async def update(self, product: Product) -> Product:
        pass

    async def delete(self, oid: str) -> Product:
        product = await self.get_by_id(oid)
        await self.repository.delete(oid)
        return product

    async def find_many(self, **kwargs) -> list[Product]:
        pass

    async def count_many(self, **kwargs) -> int:
        pass
