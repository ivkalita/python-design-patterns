from builder.computer_builder import ComputerBuilder


class DefaultComputerBuilder(ComputerBuilder):
    def get_case(self) -> None:
        self._computer.case = 'Coolermaster N300'

    def build_mainboard(self) -> None:
        self._computer.mainboard = 'MSI 970'
        self._computer.cpu = 'Intel Core i7-4770'
        self._computer.memory = 'Corsair Vengeance 16GB'

    def install_mainboard(self) -> None:
        pass

    def install_hard_drive(self) -> None:
        self._computer.hard_drive = 'Seagate 2TB'

    def install_video_card(self) -> None:
        self._computer.video_card = 'GeForce GTX 1070'
