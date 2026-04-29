import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def main():
    shapes = [
        Rectangle(10, 5),
        Square(7),
        Circle(3),
        Triangle(6, 4)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area()}")

if __name__ == "__main__":
    main()

