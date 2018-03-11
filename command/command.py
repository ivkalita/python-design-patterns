import abc
from typing import List


class Command(metaclass=abc.ABCMeta):
    _cli_args: List[str] = []

    def __init__(self, *args: List[str]) -> None:
        """ Creates a command instance. """
        self._cli_args = args

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """ The command name. """

    @property
    @abc.abstractmethod
    def description(self) -> str:
        """ The command description. """

    @abc.abstractmethod
    def execute(self, **kwargs) -> None:
        """
        Main command entry point.

        :param kwargs: command-line arguments
        """
