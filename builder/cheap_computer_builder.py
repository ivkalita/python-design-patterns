from builder.computer_builder import ComputerBuilder


class CheapComputerBuilder(ComputerBuilder):
    def get_case(self) -> None:
        self._computer.case = 'IN WIN BP655'

    def build_mainboard(self) -> None:
        self._computer.mainboard = 'ASRock AM1H-ITX'
        self._computer.cpu = 'AMD Athlon 5150'
        self._computer.memory = 'Kingston ValueRAM 4GB'

    def install_mainboard(self) -> None:
        pass

    def install_hard_drive(self) -> None:
        self._computer.hard_drive = 'WD Blue 1TB'

    def install_video_card(self) -> None:
        self._computer.video_card = 'On board'