from dataclasses import dataclass

from src.domain.entities import Product
from src.domain.services import IProductService
from src.gateways.mongodb.dto import ProductDto
from src.gateways.mongodb.repositories import IProductRepository


@dataclass
class MongoProductService(IProductService):
    repository: IProductRepository

    async def get_by_id(self, oidstr) -> Product:
        pass

    async def create(self, product: Product) -> Product:
        dto = ProductDto.from_entity(product)
        dto = await self.repository.create(dto)
        return dto.to_entity()

    async def update(self, product: Product) -> Product:
        pass

    async def delete(self, oid: str) -> Product:
        pass

    async def find_many(self, **kwargs) -> list[Product]:
        pass

    async def count_many(self, **kwargs) -> int:
        pass
