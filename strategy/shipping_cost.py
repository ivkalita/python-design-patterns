from strategy.strategy import Strategy


class ShippingCost:
    def __init__(self, strategy: Strategy) -> None:
        self.__strategy = strategy

    def shipping_cost(self, order) -> float:
        return self.__strategy.calculate(order)
