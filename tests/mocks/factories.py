from polyfactory.factories import DataclassFactory

from src.domain.commands import (
    CreateProductCommand,
    GetProductCommand,
    UpdateProductCommand,
)
from src.domain.entities import Product


class ProductFactory(DataclassFactory[Product]):
    __model__ = Product


class GetProductCommandFactory(DataclassFactory[GetProductCommand]):
    __model__ = GetProductCommand


class CreateProductCommandFactory(DataclassFactory[CreateProductCommand]):
    __model__ = CreateProductCommand


class UpdateProductCommandFactory(DataclassFactory[UpdateProductCommand]):
    __model__ = UpdateProductCommand
