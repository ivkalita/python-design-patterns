import abc
from typing import Dict, Type


class SingletonBase(metaclass=abc.ABCMeta):
    _instances: Dict[Type['SingletonBase'], 'SingletonBase'] = {}

    def __new__(cls: Type['SingletonBase'], *args, **kwargs) -> 'SingletonBase':
        if cls not in SingletonBase._instances:
            instance = super().__new__(cls)
            SingletonBase._instances[cls] = instance
        return SingletonBase._instances[cls]

