# Example of 'Abstract Factory' design pattern

from __future__ import annotations
from abc import ABC, abstractmethod


class MilitaryFactory(ABC):
    """Abstract Factory"""

    @abstractmethod
    def create_infantry_unit(self) -> InfantryUnit:
        pass

    @abstractmethod
    def create_land_unit(self) -> LandUnit:
        pass

    @abstractmethod
    def create_air_unit(self) -> AirUnit:
        pass


class BlueMilitaryFactory(MilitaryFactory):
    """Concrete factory A"""

    def create_infantry_unit(self) -> Rifleman:
        return Rifleman(25)

    def create_land_unit(self) -> Tank:
        return Tank(200)

    def create_air_unit(self) -> Helicopter:
        return Helicopter(100)


class RedMilitaryFactory(MilitaryFactory):
    """Concrete factory A"""

    def create_infantry_unit(self) -> Rifleman:
        return Rifleman(50)

    def create_land_unit(self) -> Tank:
        return Tank(175)

    def create_air_unit(self) -> Helicopter:
        return Helicopter(90)


class InfantryUnit:
    """Abstract Product A"""

    def __init__(self, life: int) -> None:
        self.life = life

    def __str__(self) -> str:
        return f'{type(self).__name__} with {self.life} life points'


class LandUnit:
    """Abstract Product B"""

    def __init__(self, life: int):
        self.life = life

    def __str__(self):
        return f'{type(self).__name__} with {self.life} life points'


class AirUnit:
    """Abstract Product C"""

    def __init__(self, life: int):
        self.life = life

    def __str__(self):
        return f'{type(self).__name__} with {self.life} life points'


class Rifleman(InfantryUnit):
    """Concrete Product A1"""


class Tank(LandUnit):
    """Concrete Product B1"""


class Helicopter(AirUnit):
    """Concrete Product C1"""


if __name__ == '__main__':
    red_factory = RedMilitaryFactory()
    blue_factory = BlueMilitaryFactory()

    red_infantry_unit = red_factory.create_infantry_unit()
    red_land_unit = red_factory.create_land_unit()
    red_air_unit = red_factory.create_air_unit()

    blue_infantry_unit = blue_factory.create_infantry_unit()
    blue_land_unit = blue_factory.create_land_unit()
    blue_air_unit = blue_factory.create_air_unit()

    print(red_infantry_unit)
    print(red_land_unit)
    print(red_air_unit)

    print(blue_infantry_unit)
    print(blue_land_unit)
    print(blue_air_unit)
