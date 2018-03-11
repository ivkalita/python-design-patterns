import abc

from factory.cars.car import Car


class Factory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_car(self) -> Car:
        """ Creates a car. """
