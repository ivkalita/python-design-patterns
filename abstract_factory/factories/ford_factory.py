from abstract_factory.cars.ford import FordEconomy, FordSport, FordLuxury
from abstract_factory.factories.factory import Factory


class FordFactory(Factory):
    def create_economy(self) -> FordEconomy:
        return FordEconomy()

    def create_sport(self) -> FordSport:
        return FordSport()

    def create_luxury(self) -> FordLuxury:
        return FordLuxury()
