"""
**Exercise 4: Polymorphism**

1. Create a class Shape with a method area() that raises a NotImplementedError.
2. Create two subclasses Circle and Rectangle that implement the area() method.
3. Write a function that takes a Shape object and prints its area. Test it with instances of Circle and Rectangle.
"""
from math import pi


class Shape():
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, heigth, width ):
        super().__init__()
        self.heigth = heigth
        self.width = width
    
    def area(self):
        return self.heigth * self.width

def print_area(shape):
    result = shape.area()
    print(result)
 
circle = Circle(56)
rectangle = Rectangle(56, 58)
print_area(circle)
print_area(rectangle)