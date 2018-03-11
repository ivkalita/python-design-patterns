import abc

from abstract_factory.cars.car import SportCar, EconomyCar, LuxuryCar


class Factory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_sport(self) -> SportCar:
        """ Creates sport car. """

    @abc.abstractmethod
    def create_economy(self) -> EconomyCar:
        """ Creates economy car. """

    @abc.abstractmethod
    def create_luxury(self) -> LuxuryCar:
        """ Creates luxury car. """
