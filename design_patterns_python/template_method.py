# Example of 'Template-method' design pattern

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """Abstract Class"""

    @abstractmethod
    def do_something(self) -> None:
        pass

    @abstractmethod
    def do_something_else(self) -> None:
        pass

    def template_method(self) -> None:
        self.do_something()
        self.do_something_else()


class FirstClass(AbstractClass):
    """Concrete Class A"""

    def do_something(self) -> None:
        print('FirstClass.do_something was called')

    def do_something_else(self) -> None:
        print('FirstClass.do_something_else was called')


class SecondClass(AbstractClass):
    """Concrete Class B"""

    def do_something(self) -> None:
        print('SecondClass.do_something was called')

    def do_something_else(self) -> None:
        print('SecondClass.do_something_else was called')


if __name__ == '__main__':
    first = FirstClass()
    first.template_method()

    second = SecondClass()
    second.template_method()
