from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import AsyncIterable

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
    async def find_many(
        self,
        sort_field: str,
        sort_order: int,
        offset: int,
        limit: int,
        search: str | None = None,
    ) -> AsyncIterable[ProductDto]:
        pass

    @abstractmethod
    async def count_many(self, search: str | None = None) -> int:
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

    def _build_find_guery(self, search: str | None = None) -> dict:
        query = {}

        if search:
            search_query = {
                "name": {"$regex": search},
                "description": {"$regex": search},
            }
            query.update(search_query)

        return query

    async def find_many(
        self,
        sort_field: str,
        sort_order: int,
        offset: int,
        limit: int,
        search: str | None = None,
    ) -> AsyncIterable[ProductDto]:
        query = self._build_find_guery(search)
        cursor = (
            self.collection.find(query)
            .sort(sort_field, sort_order)
            .skip(offset)
            .limit(limit)
        )
        async for document in cursor:
            yield ProductDto.load(document)

    async def count_many(self, search: str | None = None) -> int:
        query = self._build_find_guery(search)
        return await self.collection.count_documents(query)
