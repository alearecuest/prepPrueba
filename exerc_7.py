#!/usr/bin/python3
"""
### **Exercise 7: Method Overriding**

1. Create a class `Employee` with:
   - Attributes: `name`, `salary`
   - Method `get_details()` to print employee details.
2. Create a subclass `Manager` that overrides the `get_details()`
method to include additional information (e.g., team size).
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"The employee name is: {self.name} and his salary is: {self.salary}")
