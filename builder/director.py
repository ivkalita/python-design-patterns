from builder.computer import Computer
from builder.computer_builder import ComputerBuilder


class Director:
    def __init__(self, builder: ComputerBuilder) -> None:
        self._builder = builder

    def build_computer(self) -> None:
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.build_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()

    def get_computer(self) -> Computer:
        return self._builder.get_computer()


