from abc import ABC, abstractmethod

from src.domain.entities import Product


class IProductService(ABC):
    @abstractmethod
    async def get_by_id(self, oidstr) -> Product:
        pass

    @abstractmethod
    async def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    async def update(self, product: Product) -> Product:
        pass

    @abstractmethod
    async def delete(self, oid: str) -> Product:
        pass

    @abstractmethod
    async def find_many(self, **kwargs) -> list[Product]:
        pass

    @abstractmethod
    async def count_many(self, **kwargs) -> int:
        pass
