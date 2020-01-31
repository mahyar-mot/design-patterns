from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_opertaion(self)->str:
        product = self.factory_method()
        result = "Creator: The same creator's code has just worked with {}".format(product.operation())
        return result


class ConcreteCretor1(Creator):

    def factory_method(self)->ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self)->ConcreteProduct2:
        return ConcreteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self)->str:
        pass


class ConcreteProduct1(Product):

    def operation(self)->str:
        return "{Result of the ConcreteProduct1 }"


class ConcreteProduct2(Product):

    def operation(self)->str:
        return "{ Result of The ConcreteProduct2 }"


def client_code(creator: Creator)->None:
    print("Client: I'm not aware of the creator's class, but it still works. \n"
          "{}".format(creator.some_opertaion()))


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1 ")
    client_code(ConcreteCretor1())
    print("\n")

    print("App: Launched with the ConcreteCreator2")
    client_code(ConcreteCreator2())