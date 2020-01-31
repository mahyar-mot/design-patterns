class ShapeInterFace:
    def draw(self):
        pass


class Circle(ShapeInterFace):
    def draw(self):
        print("circle.draw")


class Square(ShapeInterFace):
    def draw(self):
        print("square.draw")


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == "circle":
            return Circle()
        if type == 'square':
            return Square()
        assert 0, 'Could not Found Shape ' + str(type)
