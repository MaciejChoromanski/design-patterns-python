# Example of 'Decorator' design pattern

from abc import ABC, abstractmethod
from typing import List


class ObjectFromLibrary(ABC):
    """Component"""

    _amount: int = None

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, amount: int) -> None:
        self._amount = amount

    @abstractmethod
    def show(self) -> None:
        pass


class Book(ObjectFromLibrary):
    """Concrete Component A"""

    def __init__(self, author: str, title: str, amount: int) -> None:
        self._author = author
        self._title = title
        self.amount = amount

    def show(self) -> None:
        print(
            f'---Book---\n'
            f'Author: {self._author}\n'
            f'Title: {self._title}\n'
            f'Amount: {self.amount}\n'
        )


class Movie(ObjectFromLibrary):
    """Concrete Component B"""

    def __init__(
            self, director: str, title: str, amount: int, length: float
    ) -> None:
        self._director = director
        self._title = title
        self.amount = amount
        self._length = length

    def show(self) -> None:
        print(
            f'---Movie---\n'
            f'Author: {self._director}\n'
            f'Title: {self._title}\n'
            f'Amount: {self.amount}\n'
            f'Length: {self._length}\n'
        )


class Decorator(ObjectFromLibrary):
    """Decorator"""

    _component: ObjectFromLibrary = None

    def __init__(self, component: ObjectFromLibrary) -> None:
        self._component = component

    @property
    def component(self) -> ObjectFromLibrary:
        return self._component

    def show(self) -> None:
        self._component.show()


class Rentable(Decorator):
    """Concrete Decorator A"""

    _renters: List[str] = []

    def rent_object(self, renter) -> None:
        self._renters.append(renter)
        self.component.amount -= 1

    def return_object(self, renter) -> None:
        self._renters.remove(renter)
        self.component.amount += 1

    def show(self) -> None:
        super().show()
        for renter in self._renters:
            print(f'Renter: {renter}')


if __name__ == '__main__':
    book = Book('Eric Matthes', 'Python Crash Course', 2)
    book.show()
    movie = Movie('Joe Johnston', 'Jumanji', 3, 2.05)
    movie.show()

    rentable_movie = Rentable(movie)
    rentable_movie.rent_object('Renter no. 1')
    rentable_movie.rent_object('Renter no. 2')
    rentable_movie.return_object('Renter no. 1')
    rentable_movie.show()
