from typing import Type

from strategy.order import Order
from strategy.shipping_cost import ShippingCost
from strategy.strategy import FedExStrategy, Strategy, PostalStrategy, UPSStrategy


class TestCase:
    @classmethod
    def setup_class(cls) -> None:
        cls.order = Order()

    def _test_strategy(self, cls: Type[Strategy], expected_cost: float) -> None:
        strategy = cls()
        cost = ShippingCost(strategy)
        assert cost.shipping_cost(self.order) == expected_cost

    def test_fed_ex_strategy(self) -> None:
        self._test_strategy(FedExStrategy, 3.00)

    def test_postal_strategy(self) -> None:
        self._test_strategy(PostalStrategy, 5.00)

    def test_ups_strategy(self) -> None:
        self._test_strategy(UPSStrategy, 4.00)
