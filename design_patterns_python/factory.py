# Example of 'Factory' design pattern


from __future__ import annotations
from abc import ABC, abstractmethod


class Sales(ABC):
    """Creator"""

    @abstractmethod
    def create_sales_document(self) -> Order:
        pass


class IndividualSales(Sales):
    """Concrete Creator A"""

    def create_sales_document(self) -> OrderA:
        return OrderA('Pencil', 5)


class BusinessSales(Sales):
    """Concrete Creator B"""

    def create_sales_document(self) -> OrderB:
        return OrderB('Pen', 200)


class Order(ABC):
    """Product"""

    def __init__(self, name: str, amount: int) -> None:
        self.name = name
        self.amount = amount


class OrderA(Order):
    """Concrete Product A"""


class OrderB(Order):
    """Concrete Product B"""


if __name__ == '__main__':
    sales = [IndividualSales(), BusinessSales()]
    for sale in sales:
        order = sale.create_sales_document()
        print(f'Created order: {order.name}, amount: {order.amount}')
