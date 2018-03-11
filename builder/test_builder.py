from typing import Type

from builder.cheap_computer_builder import CheapComputerBuilder
from builder.computer_builder import ComputerBuilder
from builder.default_computer_builder import DefaultComputerBuilder
from builder.director import Director


class TestBuilder:
    def assert_computer_built(self, builder: Type[ComputerBuilder], expected: dict) -> None:
        builder = builder()
        director = Director(builder)
        director.build_computer()
        computer = director.get_computer()
        for prop in expected:
            assert getattr(computer, prop, None) == expected[prop]

    def test_cheap_computer(self) -> None:
        self.assert_computer_built(CheapComputerBuilder, {
            'case': 'IN WIN BP655',
            'mainboard': 'ASRock AM1H-ITX',
            'cpu': 'AMD Athlon 5150',
            'memory': 'Kingston ValueRAM 4GB',
            'hard_drive': 'WD Blue 1TB',
            'video_card': 'On board'
        })

    def test_default_computer(self) -> None:
        self.assert_computer_built(DefaultComputerBuilder, {
            'case': 'Coolermaster N300',
            'mainboard': 'MSI 970',
            'cpu': 'Intel Core i7-4770',
            'memory': 'Corsair Vengeance 16GB',
            'hard_drive': 'Seagate 2TB',
            'video_card': 'GeForce GTX 1070'
        })
