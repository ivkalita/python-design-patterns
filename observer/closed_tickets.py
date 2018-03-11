from typing import Optional

from observer.kpis import KPIs
from observer.lib import Observer


class ClosedTickets(Observer):
    _source: KPIs
    _total: int = 0

    def __init__(self, source: KPIs):
        self._source = source
        self._source.attach(self)

    def update(self, value: Optional[any] = None) -> None:
        self._total += self._source.closed_tickets
        self.display()

    def display(self) -> None:
        print('Tickets closed: {}'.format(self._total))

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._source.detach(self)
