from dataclasses import dataclass

from src.domain.commands import (
    CreateProductCommand,
    DeleteProductCommand,
    GetProductCommand,
    UpdateProductCommand,
)
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

    async def execute(self, command: GetProductCommand) -> Product:
        return await self.product_service.get_by_id(command.oid)


@dataclass
class CreateProductUseCase:
    product_service: IProductService

    async def execute(self, command: CreateProductCommand) -> Product:
        return await self.product_service.create(command.product)


@dataclass
class UpdateProductUseCase:
    product_service: IProductService

    async def execute(self, command: UpdateProductCommand) -> Product:
        return await self.product_service.update(command.product)


@dataclass
class DeleteProductUseCase:
    product_service: IProductService

    async def execute(self, command: DeleteProductCommand) -> Product:
        return await self.product_service.delete(command.oid)
