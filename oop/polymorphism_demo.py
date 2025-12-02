# polymorphism_demo.py

import math

class Shape:
    """Base class representing a generic shape."""

    def area(self):
        """Method meant to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """Rectangle shape that inherits from Shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Override area to calculate rectangle area."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape that inherits from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Override area to calculate circle area."""
        return math.pi * (self.radius ** 2)

