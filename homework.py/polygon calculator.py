





from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return super().area()
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    square = Square(4)
    triangle = Triangle(6, 3)

    print("Rectangle area:", rect.area())
    print("Square area:", square.area())
    print("Triangle area:", triangle.area())
