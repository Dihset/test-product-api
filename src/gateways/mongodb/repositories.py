from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.gateways.mongodb.database import Database
from src.gateways.mongodb.dto import ProductDto


@dataclass
class IProductRepository(ABC):
    database: Database
    collection_name: str = "products"

    @property
    def collection(self):
        return self.database.connection[self.collection_name]

    @abstractmethod
    async def get_by_id(self, oidstr) -> ProductDto | None:
        pass

    @abstractmethod
    async def create(self, product: ProductDto) -> ProductDto:
        await self.collection.insert_one(product.dump())
        return product

    @abstractmethod
    async def update(self, product: ProductDto) -> None:
        pass

    @abstractmethod
    async def delete(self, oid: str) -> None:
        pass

    @abstractmethod
    async def find_many(self, **kwargs) -> list[ProductDto]:
        pass

    @abstractmethod
    async def count_many(self, **kwargs) -> int:
        pass


class MongoProductRepository(IProductRepository):
    async def get_by_id(self, oid: str) -> ProductDto | None:
        doc = await self.collection.find_one({"oid": oid})
        return ProductDto.load(doc)

    async def create(self, product: ProductDto) -> ProductDto:
        await self.collection.insert_one(product.dump())
        return product

    async def update(self, product: ProductDto) -> None:
        await self.collection.update_one(
            {"oid": product.oid}, 
            {"$set": product.dump()},
        )

    async def delete(self, oid: str) -> None:
        await self.collection.delete_one({"oid": oid})

    async def find_many(self, **kwargs) -> list[ProductDto]:
        pass

    async def count_many(self, **kwargs) -> int:
        pass
