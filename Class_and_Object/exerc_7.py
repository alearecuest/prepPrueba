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
        return (f"The employee name is: {self.name} and his salary is: U$S {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department, team_size, position):
        super().__init__(name, salary)
        self.department = department
        self.team_size = team_size
        self.position = position
    
    def get_details(self):
        basic_details = super().get_details()
        return f"{basic_details}, Department: {self.department}, Team Size: {self.team_size}, Position: {self.position}"

Emanuel = Manager("Emanuel", "75890", "Educator", 10, "Teacher")
Alejandro = Manager("Alejandro", "98000", "Full Stack", 10, "Programmer")

print(f"Emanuel: {Emanuel.get_details()}")
print(f"Alejandro: {Alejandro.get_details()}")
