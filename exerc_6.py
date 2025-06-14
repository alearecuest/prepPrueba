#!/usr/bin/python3
"""
### **Exercise 6: Class vs Instance Attributes**

1. Create a class `Person` with:
   - A class attribute `species` set to "Homo sapiens"
   - Instance attributes `name` and `age`
2. Show how to access and modify the class attribute and the instance attributes.
"""


class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

species1 = Person("Betty", 108)
species2 = Person("Cape", 28)

print("\n=== INSTANCE ATTRIBUTES ===")
print("Accesing instance attributes:")

print(f"Name person 1: {species1.name}, Age: {species1.age} years")
print(f"Name person 2: {species2.name}, Age: {species2.age} years")

print("\nModifying instance attributes:")
species1.age = 80
print(f"After modification age, new age: {species1.age} years, age of second person remains: {species2.age} years")

print("\n=== CLASS ATTRIBUTES ===")
print("Accessing class attribute:")
print(f"Person.species: {Person.species}")
print(f"person1.species: {species1.species}")
print(f"person2.species: {species2.species}")

print("\nModifying class attribute through the class:")
species1.species = "Homo sapiens sapiens"

print(f"After Person.species = 'Homo sapiens sapiens':")
print(f"Person.species: {Person.species}")
print(f"person1.species: {species1.species}")
print(f"person2.species: {species2.species}")

print("\nModifying attribute on a specific instance:")
species1.species = "Homo digitalis"
print(f"After person1.species = 'Homo digitalis':")
print(f"Person.species: {Person.species}")
print(f"person1.species: {species1.species}")
print(f"person2.species: {species2.species}")