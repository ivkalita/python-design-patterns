from typing import Optional, Tuple

import pytest
from _pytest.capture import CaptureFixture

from observer.closed_tickets import ClosedTickets
from observer.kpis import KPIs
from observer.kpis_display import KPIsDisplay


class TestObserver:
    _capsys: CaptureFixture = None

    @pytest.fixture(scope='function', autouse=True)
    def before_each(self, capsys: CaptureFixture) -> None:
        self._capsys = capsys
        capsys.readouterr()

    def assert_printed(self, kpis: Optional[Tuple[int, int, int]], closed: Optional[int]) -> None:
        out, _ = self._capsys.readouterr()
        part_1 = 'Tickets closed: {}\n'.format(closed) if closed else ''
        part_2 = 'Current KPIs:\nopened = {}\nclosed = {}\nnew = {}\n'.format(kpis[0], kpis[1], kpis[2]) if kpis else ''
        assert part_1 + part_2 == out or part_2 + part_1 == out

    def test_kpis_changes(self) -> None:
        with KPIs() as kpis:
            with ClosedTickets(kpis):
                with KPIsDisplay(kpis):
                    kpis.set_kpis(1, 2, 3)
                    self.assert_printed(kpis=(1, 2, 3), closed=2)

                    kpis.set_kpis(0, 1, 0)
                    self.assert_printed(kpis=(0, 1, 0), closed=3)

                kpis.set_kpis(0, 2, 0)
                self.assert_printed(kpis=None, closed=5)

            kpis.set_kpis(1, 2, 3)
            self.assert_printed(kpis=None, closed=None)
