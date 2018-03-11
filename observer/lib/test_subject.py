import warnings
from unittest import mock

import pytest

from observer.lib import Observer
from observer.lib import Subject


class ConcreteSubject(Subject):
    pass


class TestSubject:
    subject: ConcreteSubject = None

    @pytest.fixture(scope='function', autouse=True)
    def before_each(self):
        self.subject = ConcreteSubject()

    def test_attached_observer_notified(self) -> None:
        observer = mock.MagicMock(spec=Observer)
        with self.subject:
            self.subject.attach(observer)
            self.subject.notify('some value')
            observer.update.assert_called_once_with('some value')

    def test_observers_detached_after_usage(self) -> None:
        observer = mock.MagicMock(spec=Observer)
        with self.subject:
            self.subject.attach(observer)
        self.subject.notify('some value')
        observer.update.assert_not_called()

    def test_explicitly_detached_observer_not_notified(self) -> None:
        observer = mock.MagicMock(spec=Observer)
        with self.subject:
            self.subject.attach(observer)
            self.subject.detach(observer)
            self.subject.notify('some value')
            observer.update.assert_not_called()

    def test_repeatable_detach(self) -> None:
        observer = mock.MagicMock(spec=Observer)
        with self.subject:
            self.subject.detach(observer)
            self.subject.detach(observer)
