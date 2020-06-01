# Example of 'Builder' design pattern


from __future__ import annotations
from abc import ABC, abstractmethod


class Player:
    """Product"""

    _name: str = None

    def set_name(self, name: str) -> None:
        self._name = name

    def show(self) -> None:
        print(self._name)


class PlayerBuilder(ABC):
    """Builder"""

    @property
    @abstractmethod
    def player(self) -> Player:
        pass

    @abstractmethod
    def build_player(self) -> None:
        pass


class FlashPlayerCreator(PlayerBuilder):
    """Concrete builder A"""

    _player: Player = Player()

    @property
    def player(self) -> Player:
        return self._player

    def build_player(self) -> None:
        self._player.set_name('Flash Player')


class HTMLPlayerCreator(PlayerBuilder):
    """Concrete builder B"""

    _player: Player = Player()

    @property
    def player(self) -> Player:
        return self._player

    def build_player(self) -> None:
        self._player.set_name('HTML Player')


class Generator:
    """Director"""

    def build(self, player_builder: PlayerBuilder) -> None:
        player_builder.build_player()


if __name__ == '__main__':
    html_creator = HTMLPlayerCreator()
    flash_creator = FlashPlayerCreator()
    generator = Generator()

    generator.build(html_creator)
    html_creator.player.show()

    generator.build(flash_creator)
    flash_creator.player.show()
