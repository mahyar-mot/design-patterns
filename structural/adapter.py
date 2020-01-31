class Target:

    def request(self)->str:
        return "Target the defult target's behavior "


class Adaptee:

    def specific_request(self)->str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter:

    def __init__(self, adaptee:Adaptee)->None:
        self.adaptee = adaptee

    def request(self)->str:
        return "Adapter: (TRANSLATE) {}".format(self.adaptee.specific_request()[::-1])


def client_code(target:Target)->None:
    print(target.request())


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
