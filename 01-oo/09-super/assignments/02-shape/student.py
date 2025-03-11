from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
    @property
    def area(self):
        return self._length * self._width
    
    @property
    def perimeter(self):
        return 2 * (self._length + self._width)
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        return self.length
    
class Ellipse(Shape):
    def __init__(self, major_radius, minor_radius):
        self._major_radius = major_radius
        self._minor_radius = minor_radius

    @property
    def major_radius(self):
        return self._major_radius # major_radius is read-only
    
    @property
    def minor_radius(self):
        return self._minor_radius # minor_radius is read-only
    
    @property
    def area(self):
        return pi * self._major_radius * self._minor_radius
    
    @property
    def perimeter(self):
        raise NotImplementedError("Perimeter of an ellipse is not trivial to calculate")
    
class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)

    @property
    def radius(self):
        return self.major_radius
    
    @property
    def perimeter(self):
        return 2 * pi * self.major_radius
    
# Test code
"""
if __name__ == "__main__":
    # Test Square
    square = Square(4)
    print(f"Square - Side: {square.side}, Area: {square.area}, Perimeter: {square.perimeter}")

    # Test Rectangle
    rect = Rectangle(5, 3)
    print(f"Rectangle - Length: {rect.length}, Width: {rect.width}, Area: {rect.area}, Perimeter: {rect.perimeter}")

    # Test Circle
    circle = Circle(3)
    print(f"Circle - Radius: {circle.radius}, Area: {circle.area}, Perimeter: {circle.perimeter}")

    # Test Ellipse (perimeter zal een fout veroorzaken)
    ellipse = Ellipse(5, 3)
    print(f"Ellipse - Major Radius: {ellipse.major_radius}, Minor Radius: {ellipse.minor_radius}, Area: {ellipse.area}")
    
    try:
        print(ellipse.perimeter)
    except NotImplementedError as e:
        print(f"Error: {e}")  # Verwachte fout
"""   
