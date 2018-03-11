import abc
import warnings
from typing import Optional, Set

from observer.lib import Observer


class Subject(metaclass=abc.ABCMeta):
    """ Abstract event producer. """

    _observers: Set[Observer] = set()

    def attach(self, observer: Observer) -> None:
        """ Attaches new observer to the subject. """
        self._observers.add(observer)

    def detach(self, observer: Observer) -> None:
        """ Detaches observer from the subject. """
        if observer not in self._observers:
            warnings.warn('Observer {} was not attached to a Subject {}'.format(observer, self))
        else:
            self._observers.remove(observer)

    def notify(self, value: Optional[any] = None) -> None:
        """ Sends event changes to all attached observers. """
        for observer in self._observers:
            observer.update(value)

    def __enter__(self) -> 'Subject':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ Clear all observers to prevent dangling references. """
        self._observers.clear()
