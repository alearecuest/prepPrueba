#!/usr/bin/python3
"""
### **Exercise 8: Static and Class Methods**

1. Create a class `Calculator` with:
   - A static method `add(a, b)` that returns the sum of two numbers.
   - A class method `create_default()` that returns a default instance of `Calculator`.
2. Demonstrate the usage of both methods.
"""


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def create_default(cls):
        return cls()

calc1 = Calculator.add(2, 3.4)
calc2 = Calculator.create_default()

print(f"The value is: {calc1}")
print(f"The new instance is: {calc2}")