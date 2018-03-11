from inspect import getmembers, isclass, isabstract

from factory.factories.factory import Factory


def load_factory(factory_name: str) -> Factory:
    """ Instantiates factory based on its name. """
    try:
        factory_module = __import__('factory.factories.{}'.format(factory_name))
    except ImportError:
        factory_name = 'null_factory'
        factory_module = __import__('factory.factories.null_factory')

    factory_module = getattr(factory_module.factories, factory_name)

    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m) and issubclass(m, Factory))

    return classes[0][1]()
