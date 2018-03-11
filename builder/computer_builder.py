import abc

from builder.computer import Computer


class ComputerBuilder(metaclass=abc.ABCMeta):
    _computer: Computer = None

    def new_computer(self) -> None:
        self._computer = Computer()

    def get_computer(self) -> Computer:
        return self._computer

    @abc.abstractmethod
    def get_case(self) -> None:
        """ Setups computer's case. """

    @abc.abstractmethod
    def build_mainboard(self) -> None:
        """ Builds computer's mainboard. """

    @abc.abstractmethod
    def install_mainboard(self) -> None:
        """ Installs computer's mainboard. """

    @abc.abstractmethod
    def install_hard_drive(self) -> None:
        """ Installs hard drive. """

    @abc.abstractmethod
    def install_video_card(self) -> None:
        """ Installs video card. """
