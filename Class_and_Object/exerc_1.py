#!/usr/bin/python3
'''### **Exercise 1: Basic Class and Object**
1. Create a class Car with the following attributes:
   - brand
   - model
   - year
2. Add a method display_info() to print the details of the car.
3. Instantiate an object of the Car class and call the display_info() method.
'''


class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Atributos del coche")
        print(f"Marca: {self.brand}\nModelo: {self.model}\nAño: {self.year}")

auto = Car("Fiat", "OneWay", "2025")
auto.display_info()
