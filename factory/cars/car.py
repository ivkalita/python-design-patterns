import abc


class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def stop(self) -> None:
        """ Stops the car. """

    @abc.abstractmethod
    def start(self) -> None:
        """ Starts the car. """
