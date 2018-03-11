from singleton.singleton_meta import SingletonMeta


class ConcreteSingletonMeta(metaclass=SingletonMeta):
    pass


class AnotherConcreteSingletonMeta(metaclass=SingletonMeta):
    pass


class TestSingletonMeta:
    def test_create(self) -> None:
        a = ConcreteSingletonMeta()
        assert a is not None
        assert isinstance(a, ConcreteSingletonMeta)

    def test_multiple_creation(self) -> None:
        a = ConcreteSingletonMeta()
        b = ConcreteSingletonMeta()
        assert a is b

    def test_different_singletons(self) -> None:
        a1 = ConcreteSingletonMeta()
        a2 = ConcreteSingletonMeta()
        b1 = AnotherConcreteSingletonMeta()
        b2 = AnotherConcreteSingletonMeta()

        assert a1 is a2
        assert b1 is b2
        assert a1 is not b1
