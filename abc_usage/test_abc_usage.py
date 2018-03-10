import pytest

from abc_usage.good_class import GoodClass


class TestCase:
    def test_bad_class_raises(self) -> None:
        with pytest.raises(TypeError) as e:
            from abc_usage.bad_class import BadClass
            BadClass()

    def test_good_class_not_raises(self) -> None:
        GoodClass()

    def test_good_class(self) -> None:
        instance = GoodClass()
        assert instance.is_running is False
        instance.run()
        assert instance.is_running is True
        instance.stop()
        assert instance.is_running is False
