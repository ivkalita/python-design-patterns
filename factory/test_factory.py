from factory.cars.jeep import Jeep
from factory.cars.null_car import NullCar
from factory.cars.van import Van
from factory.loader import load_factory


class TestFactory:
    def test_jeep_created(self) -> None:
        factory = load_factory('jeep_factory')
        car = factory.create_car()
        assert isinstance(car, Jeep)

    def test_van_created(self) -> None:
        factory = load_factory('van_factory')
        car = factory.create_car()
        assert isinstance(car, Van)

    def test_null_car_created(self) -> None:
        factory = load_factory('unknown_car_factory')
        car = factory.create_car()
        assert isinstance(car, NullCar)
