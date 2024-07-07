from polyfactory.factories import DataclassFactory

from src.domain.commands import (
    CreateProductCommand,
    DeleteProductCommand,
    GetProductCommand,
    GetProductListCommand,
    UpdateProductCommand,
)
from src.domain.entities import Product


class ProductFactory(DataclassFactory[Product]):
    __model__ = Product


class GetProductListCommandFactory(DataclassFactory[GetProductListCommand]):
    __model__ = GetProductListCommand


class GetProductCommandFactory(DataclassFactory[GetProductCommand]):
    __model__ = GetProductCommand


class CreateProductCommandFactory(DataclassFactory[CreateProductCommand]):
    __model__ = CreateProductCommand


class UpdateProductCommandFactory(DataclassFactory[UpdateProductCommand]):
    __model__ = UpdateProductCommand


class DeleteProductCommandFactory(DataclassFactory[DeleteProductCommand]):
    __model__ = DeleteProductCommand
