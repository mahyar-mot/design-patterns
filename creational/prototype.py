from __future__ import annotations
from datetime import datetime
from copy import deepcopy
from typing import Any


class Prototype:

    def __init__(self)->None:
        self._primitive = None
        self._component = None
        self._circular_refrence = None

    @property
    def primitive(self)->Any:
        return self._primitive

    @primitive.setter
    def primitive(self, value:Any)->None:
        self._primitive = value

    @property
    def component(self)->object:
        return self._component

    @component.setter
    def component(self, value:object)->None:
        self._component = value

    @property
    def circular_refrence(self)->ComponentWithBackRefrence:
        return self._circular_refrence

    @circular_refrence.setter
    def circular_refrence(self, value:ComponentWithBackRefrence)->None:
        self._circular_refrence = value

    def clone(self)->Prototype:
        self.component = deepcopy(self.component)
        self.circular_refrence = deepcopy(self.circular_refrence)
        self.circular_refrence.prototype = self
        return deepcopy(self)


class ComponentWithBackRefrence:

    def __init__(self, prototype:Prototype):
        self._prototype = prototype

    @property
    def prototype(self)->Prototype:
        return self._prototype

    @prototype.setter
    def prototype(self, value:Prototype)->None:
        self._prototype = value


if __name__ == "__main__":
    p1 = Prototype()
    p1.primitive = 245
    p1.component = datetime.now()
    p1.circular_refrence = ComponentWithBackRefrence(p1)
    p2 = p1.clone()

    if p1.primitive is p2.primitive:
        print("Primitive field values have been carried over to clone. YAY!")
    else:
        print("Primitive field values have not been carried over to clone. BOO!")

    if p1.component is p2.component:
        print("Simple Component has Not Been Cloned.BOO !")
    else:
        print("Simple Component has Been Cloned.YAY!")

    if p1.circular_refrence is p2.circular_refrence:
        print("Component with BackRefrence has not been cloned. BOO!")
    else:
        print("Component with BackRefrence has been cloned. YAY!")

    if p1.circular_refrence.prototype is p2.circular_refrence.prototype:
        print("Component with back refrence is linked to original object . BOO!")
    else:
        print("Component with back refrence is linked to the clone object . YAY!")