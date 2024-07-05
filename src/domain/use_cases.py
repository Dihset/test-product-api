from dataclasses import dataclass

from src.domain.commands import CreateProductCommand
from src.domain.entities import Product
from src.domain.services import IProductService


@dataclass
class GetProductListUseCase:
    product_service: IProductService

    async def execute(self) -> tuple[list[Product], int]:
        pass


@dataclass
class GetProductUseCase:
    product_service: IProductService

    async def execute(self) -> Product:
        pass


@dataclass
class CreateProductUseCase:
    product_service: IProductService

    async def execute(self, command: CreateProductCommand) -> Product:
        return await self.product_service.create(command.product)


@dataclass
class UpdateProductUseCase:
    product_service: IProductService

    async def execute(self) -> Product:
        pass


@dataclass
class DeleteProductUseCase:
    product_service: IProductService

    async def execute(self) -> Product:
        pass
