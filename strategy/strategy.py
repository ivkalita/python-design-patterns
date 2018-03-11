import abc

from strategy.order import Order


class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self, order: Order) -> float:
        """ Calculates order's shipping cost """


class FedExStrategy(Strategy):
    def calculate(self, order: Order) -> float:
        return 3.00


class PostalStrategy(Strategy):
    def calculate(self, order: Order) -> float:
        return 5.00


class UPSStrategy(Strategy):
    def calculate(self, order: Order) -> float:
        return 4.00
