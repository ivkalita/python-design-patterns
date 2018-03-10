import abc


class Runnable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self) -> None:
        """
        Make an instance run.
        """
        pass

    @abc.abstractmethod
    def stop(self) -> None:
        """
        Stop the instance.
        """
        pass

    @property
    @abc.abstractmethod
    def is_running(self) -> bool:
        """
        Returns true if instance is running.
        """
        pass
