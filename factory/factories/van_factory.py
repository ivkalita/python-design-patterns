from factory.cars.van import Van
from factory.factories.factory import Factory


class VanFactory(Factory):
    def create_car(self) -> Van:
        return Van()
