#!/usr/bin/python3
'''### **Exercise 2: Inheritance**
1. Create a base class Animal with:
   - Attributes: name, species
   - Method: make_sound() (prints "Some generic sound")
2. Create a subclass Dog that overrides make_sound() to print "Woof!"
3. Instantiate objects of both classes and call make_sound() for each.
'''


class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"El {self.species} llamado {self.name} hace este sonido: Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print(f"El {self.species} llamado {self.name} hace este sonido: Woof!")

gato = Animal("Odín", "Gato")
perro = Dog("Campeón", "Perro")
gato.make_sound()
perro.make_sound()
