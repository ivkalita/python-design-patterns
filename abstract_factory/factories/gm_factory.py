from abstract_factory.cars.gm import GMEconomy, GMSport, GMLuxury
from abstract_factory.factories.factory import Factory


class GMFactory(Factory):
    def create_economy(self) -> GMEconomy:
        return GMEconomy()

    def create_sport(self) -> GMSport:
        return GMSport()

    def create_luxury(self) -> GMLuxury:
        return GMLuxury()
