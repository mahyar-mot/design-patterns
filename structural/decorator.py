class Component:

    def operation(self)->str:
        pass


class ConcreteComponent(Component):

    def operation(self)->str:
        return "Concrete Component"


class Decorator(Component):

    _component:Component = None

    def __init__(self, component:Component)->None:
        self._component = component

    @property
    def component(self)->str:
        return self._component

    def operation(self)->str:
        self._component.operation()


class ConcreteDecoratorA(Decorator):

    def operation(self)->str:
        return "ConcreteDecoratorA({})".format(self.component.operation())


class ConcreteDecoratorB(Decorator):

    def operation(self)->str:
        return "ConcreteDecoratorB({})".format(self.component.operation())


def client_code(component:Component)->None:
    print("Result: {}".format(component.operation()))


if __name__ == "__main__":
    simple = ConcreteComponent()
    print("ClientL I've got a simple component")
    client_code(simple)

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)
