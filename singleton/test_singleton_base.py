from singleton.singleton_base import SingletonBase


class ConcreteSingletonBase(SingletonBase):
    pass


class AnotherConcreteSingletonBase(SingletonBase):
    pass


class TestSingletonBase:
    def test_create(self) -> None:
        a = ConcreteSingletonBase()
        assert a is not None
        assert isinstance(a, ConcreteSingletonBase)

    def test_multiple_creation(self) -> None:
        a = ConcreteSingletonBase()
        b = ConcreteSingletonBase()
        assert a is b

    def test_different_singletons(self) -> None:
        a1 = ConcreteSingletonBase()
        a2 = ConcreteSingletonBase()
        b1 = AnotherConcreteSingletonBase()
        b2 = AnotherConcreteSingletonBase()

        assert a1 is a2
        assert b1 is b2
        assert a1 is not b1
