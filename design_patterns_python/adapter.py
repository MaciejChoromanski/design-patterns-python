# Example of 'Adapter' design pattern

from abc import ABC, abstractmethod


class Sensor(ABC):
    """Target"""

    @abstractmethod
    def get_temperature(self) -> float:
        pass


class FahrenheitSensor:
    """Adaptee"""

    temperature = 99.4

    def get_temperature(self) -> float:
        return self.temperature


class Adapter(Sensor):
    """Adapter"""

    def __init__(self, fahrenheit_sensor: FahrenheitSensor) -> None:
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temperature(self) -> float:
        return (self.fahrenheit_sensor.get_temperature() - 32) * 5 / 9


if __name__ == '__main__':
    celsius = Adapter(FahrenheitSensor())
    print(f'99.4 °F = {celsius.get_temperature()} °C')
