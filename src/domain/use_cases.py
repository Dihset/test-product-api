import asyncio
from dataclasses import dataclass

from src.domain.commands import (
    CreateProductCommand,
    DeleteProductCommand,
    GetProductCommand,
    GetProductListCommand,
    UpdateProductCommand,
)
from src.domain.entities import Product
from src.domain.services import IProductService


@dataclass
class GetProductListUseCase:
    product_service: IProductService

    async def execute(
        self, command: GetProductListCommand
    ) -> tuple[list[Product], int]:
        products_task = asyncio.create_task(
            self.product_service.find_many(
                sort_field=command.sort.field,
                sort_order=command.sort.order.value,
                offset=command.pagination.offset,
                limit=command.pagination.limit,
                search=command.search,
            )
        )
        count_task = asyncio.create_task(
            self.product_service.count_many(command.search)
        )
        return await products_task, await count_task


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
