# Example of 'Command' design pattern

from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    """Command"""

    def __init__(self, receiver: Receiver) -> None:
        self._receiver = receiver

    @abstractmethod
    def run(self) -> None:
        pass


class SpecificCommand(Command):
    """Inherits from Command"""

    def run(self) -> None:
        self._receiver.perform()


class Receiver:
    """Receiver"""

    def perform(self) -> None:
        print('Receiver.perform was called')


class Invoker:
    """Invoker"""

    _command: Command = None

    def set_command(self, command: Command) -> None:
        self._command = command

    def run_command(self) -> None:
        self._command.run()


if __name__ == '__main__':
    receiver = Receiver()
    specific_command = SpecificCommand(receiver)
    invoker = Invoker()

    invoker.set_command(specific_command)
    invoker.run_command()
