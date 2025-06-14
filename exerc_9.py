#!/usr/bin/python3
### **Exercise 9: Multiple Inheritance**
"""
1. Create two classes:
   - `Flyable` with a method `fly()`
   - `Swimmable` with a method `swim()`
2. Create a class `Duck` that inherits from both `Flyable` and `Swimmable`.
3. Instantiate a `Duck` and call both methods.
"""


class Flyable:
    def fly(self):
        return "fly"

class Swimmable:
    def swim(self):
        return "swim"

class Duck(Flyable, Swimmable):
    def get_details(self):
        return f"is a duck, that can {self.fly()} and {self.swim()}!"

Donald = Duck()
Donald.fly()
Donald.swim()

print(f"Donald: {Donald.get_details()}")
