#  abstract shape classes
class Shape2DInterface:
    def draw(self):
        pass


class Shape3DInterface:
    def build(self):
        pass


# concrete shape classes
class Circle(Shape2DInterface):
    def draw(self):
        print("circle.draw")


class Square(Shape2DInterface):
    def draw(self):
        print("square.draw")


class Sphere(Shape3DInterface):
    def build(self):
        print("sphere.build")


class Cube(Shape3DInterface):
    def build(self):
        print("cube.build")


# abstract shape factory
class ShapeFactoryInterface:
    @staticmethod
    def getShape(sides):
        pass


# concrete shape factories
class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, "Bad 2d Creation shape not defined for {} sides".format(sides)


class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, "Bad 3D shape Creation : Shape not defined for {} sides".format(sides)
