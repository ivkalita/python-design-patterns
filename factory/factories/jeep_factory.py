from factory.cars.jeep import Jeep
from factory.factories.factory import Factory


class JeepFactory(Factory):
    def create_car(self) -> Jeep:
        return Jeep()
