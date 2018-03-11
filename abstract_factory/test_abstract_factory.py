from typing import Type

from abstract_factory.cars.car import EconomyCar, LuxuryCar, SportCar
from abstract_factory.factories.factory import Factory
from abstract_factory.factories.ford_factory import FordFactory
from abstract_factory.factories.gm_factory import GMFactory


class TestAbstractFactory:
    def assert_factory_creates_needed_cars(self, factory: Type[Factory]) -> None:
        instance = factory()
        assert isinstance(instance.create_economy(), EconomyCar)
        assert isinstance(instance.create_luxury(), LuxuryCar)
        assert isinstance(instance.create_sport(), SportCar)

    def test_ford_factory(self) -> None:
        self.assert_factory_creates_needed_cars(FordFactory)

    def test_gm_factory(self) -> None:
        self.assert_factory_creates_needed_cars(GMFactory)
