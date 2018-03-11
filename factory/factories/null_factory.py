from factory.cars.null_car import NullCar
from factory.factories.factory import Factory


class NullFactory(Factory):
    def create_car(self) -> NullCar:
        return NullCar()
