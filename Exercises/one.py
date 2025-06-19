"""
### **Exercise 1: Basic Class and Object**
1. Create a class Car with the following attributes:
   - brand
   - model
   - year
2. Add a method display_info() to print the details of the car.
3. Instantiate an object of the Car class and call the display_info() method.

---
"""
class Car ():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
        
fiatOne = Car("Fiat", "One", "2025")

fiatOne.display_info()