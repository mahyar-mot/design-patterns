from __future__ import annotations
from typing import Optional
from threading import Lock, Thread


class SingletonMeta(type):

    _instance : Optional[Singleton] = None

    _lock : Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):

    value : str = None

    def __init__(self, value: str)->None:
        self.value = value

    def some_business_logic(self):
        pass


def test_singleton(value: str):
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":

    print(" If You see the same value then singleton was reused! YAY If You see multiple value then singleton failed")

    process1 = Thread(target=test_singleton, args=("Foo",))
    process2 = Thread(target=test_singleton, args=("Bar",))
    process1.start()
    process2.start()
