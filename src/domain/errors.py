class BaseDomainException(Exception):
    pass


class BaseProductException(BaseDomainException):
    pass


class ProductNotFoundException(BaseProductException):
    pass
