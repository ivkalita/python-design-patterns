import abc
from typing import Optional


class Observer(metaclass=abc.ABCMeta):
    """ Abstract observer. """

    @abc.abstractmethod
    def update(self, value: Optional[any] = None):
        """ Fires, when the state of subject is changed. """

    def __enter__(self) -> 'Observer':
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ You need to detach observer in this method implementation. """
