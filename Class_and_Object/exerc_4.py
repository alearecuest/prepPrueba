#!/usr/bin/python3
'''
### **Exercise 4: Polymorphism**

1. Create a class Shape with a method area() that raises a NotImplementedError.
2. Create two subclasses Circle and Rectangle that implement the area() method.
3. Write a function that takes a Shape object and prints its area. Test it with instances of Circle and Rectangle.
'''


import math

class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def take_object(shape):
    object = shape.area()
    return object

circle = Circle(5)
rectangle = Rectangle(4, 2)
print(f"El área del Círculo es: {take_object(circle)} cm^2")
print(f"El área del Rectángulo es: {take_object(rectangle)} cm^2")
