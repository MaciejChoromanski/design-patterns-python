# Example of Abstract Factory design pattern

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractMilitaryFactory(ABC):
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


class BlueMilitaryFactory(AbstractMilitaryFactory):
    """Concrete factory A"""

    def create_infantry_unit(self) -> InfantryUnit:
        return InfantryUnit(25)

    def create_land_unit(self) -> LandUnit:
        return LandUnit(200)

    def create_air_unit(self) -> AirUnit:
        return AirUnit(100)


class RedMilitaryFactory(AbstractMilitaryFactory):
    """Concrete factory A"""

    def create_infantry_unit(self) -> InfantryUnit:
        return InfantryUnit(50)

    def create_land_unit(self) -> LandUnit:
        return LandUnit(175)

    def create_air_unit(self) -> AirUnit:
        return AirUnit(90)


class InfantryUnit:
    """Concrete Product A"""

    def __init__(self, life: int):
        self.life = life

    def __str__(self):
        return f'InfantryUnit with {self.life} life points'


class LandUnit:
    """Concrete Product B"""

    def __init__(self, life: int):
        self.life = life

    def __str__(self):
        return f'LandUnit with {self.life} life points'


class AirUnit:
    """Concrete Product C"""

    def __init__(self, life: int):
        self.life = life

    def __str__(self):
        return f'AirUnit with {self.life} life points'


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
