from typing import Optional

from observer.kpis import KPIs
from observer.lib import Observer


class KPIsDisplay(Observer):
    _source: KPIs

    opened_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, source: KPIs) -> None:
        self._source = source
        self._source.attach(self)

    def update(self, value: Optional[any] = None) -> None:
        self.opened_tickets = self._source.opened_tickets
        self.closed_tickets = self._source.closed_tickets
        self.new_tickets = self._source.new_tickets
        self.display()

    def display(self) -> None:
        print('Current KPIs:')
        print('opened = {}'.format(self.opened_tickets))
        print('closed = {}'.format(self.closed_tickets))
        print('new = {}'.format(self.new_tickets))

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._source.detach(self)
