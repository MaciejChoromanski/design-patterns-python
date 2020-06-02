# Example of 'Proxy' design pattern

from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):
    """Subject"""

    @abstractmethod
    def request(self) -> None:
        pass


class SpecificProduct(Product):
    """Real Subject"""

    def request(self) -> None:
        print('SpecificProduct.request was called')


class Proxy(Product):
    """Proxy"""

    def __init__(self, specific_product: SpecificProduct) -> None:
        self._specific_product = specific_product

    def request(self) -> None:
        print('Using Proxy')
        self._specific_product.request()


if __name__ == '__main__':
    proxy = Proxy(SpecificProduct())
    proxy.request()
