from functools import lru_cache

import punq

from src.domain.services import IProductService
from src.domain.use_cases import (
    CreateProductUseCase,
    DeleteProductUseCase,
    GetProductListUseCase,
    GetProductUseCase,
    UpdateProductUseCase,
)
from src.gateways.mongodb.database import Database
from src.gateways.mongodb.repositories import IProductRepository, MongoProductRepository
from src.services.product import MongoProductService


@lru_cache(1)
def get_container() -> punq.Container:
    """Singleton фабрика DI контейнера."""
    return init_container()


def init_container() -> punq.Container:
    container = punq.Container()

    container.register(Database, scope=punq.Scope.singleton)

    container.register(IProductRepository, MongoProductRepository)

    container.register(IProductService, MongoProductService)

    container.register(GetProductListUseCase)
    container.register(GetProductUseCase)
    container.register(CreateProductUseCase)
    container.register(UpdateProductUseCase)
    container.register(DeleteProductUseCase)

    return container
