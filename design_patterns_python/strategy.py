# Example of 'Strategy' design pattern

from __future__ import annotations

from abc import ABC, abstractmethod


class Context:
    """Context"""

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def get_problem(self) -> None:
        self._strategy.solve_problem()


class Strategy(ABC):
    """Strategy"""

    @abstractmethod
    def solve_problem(self) -> None:
        pass


class BlueStrategy(Strategy):
    """Concrete Strategy A"""

    def solve_problem(self) -> None:
        print('BlueStrategy.solve_problem was called')


class RedStrategy(Strategy):
    """Concrete Strategy B"""

    def solve_problem(self) -> None:
        print('RedStrategy.solve_problem was called')


if __name__ == '__main__':
    context = Context(BlueStrategy())
    context.get_problem()

    context = Context(RedStrategy())
    context.get_problem()
