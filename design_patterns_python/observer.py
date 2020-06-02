# Example of 'Observer' design pattern

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Observer"""

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class BlueObserver(Observer):
    """Concrete Observer A"""

    def update(self, subject: Subject) -> None:
        if subject.state < 3:
            print("BlueObserver reacted to the event")


class RedObserver(Observer):
    """Concrete Observer B"""

    def update(self, subject: Subject) -> None:
        if subject.state > 3:
            print("RedObserver reacted to the event")


class Subject(ABC):
    """Subject"""

    @property
    @abstractmethod
    def state(self) -> int:
        pass

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class SpecificSubject(Subject):
    """Concrete Subject A"""

    state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


if __name__ == '__main__':
    specific_subject = SpecificSubject()

    specific_subject.attach(BlueObserver())
    specific_subject.attach(RedObserver())

    specific_subject.state = 2
    specific_subject.notify()

    specific_subject.state = 4
    specific_subject.notify()
