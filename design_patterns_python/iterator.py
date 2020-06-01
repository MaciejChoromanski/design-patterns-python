# Example of 'Iterator' design pattern


from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List


class NameIterator(Iterator):
    """Iterator"""

    _position: int = None

    def __init__(self, collection: List[str]) -> None:
        self._collection = collection
        self._position = 0

    def __next__(self) -> str:
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value


class NameCollection(Iterable):
    """Iterable"""

    def __init__(self, collection: List[str] = None) -> None:
        self._collection = collection or []

    def __iter__(self) -> NameIterator:
        return NameIterator(self._collection)


if __name__ == '__main__':
    name_collection = NameCollection(['Stan', 'Kyle', 'Eric', 'Kenny'])
    for name in name_collection:
        print(name)
