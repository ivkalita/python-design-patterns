from observer.lib import Subject


class KPIs(Subject):
    _opened_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    @property
    def opened_tickets(self) -> int:
        return self._opened_tickets

    @property
    def closed_tickets(self) -> int:
        return self._closed_tickets

    @property
    def new_tickets(self) -> int:
        return self._new_tickets

    def set_kpis(self, opened_tickets: int, closed_tickets: int, new_tickets: int) -> None:
        self._opened_tickets = opened_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()
