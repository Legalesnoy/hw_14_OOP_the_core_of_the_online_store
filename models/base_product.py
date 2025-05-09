from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """родительский класс для класса продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
