"""
**Exercise 2: Inheritance**
1. Create a base class Animal with:
   - Attributes: name, species
   - Method: make_sound() (prints "Some generic sound")
2. Create a subclass Dog that overrides make_sound() to print "Woof!"
3. Instantiate objects of both classes and call make_sound() for each.
"""
class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def make_sound(self):
        print("Woof!")

bird = Animal("Piolín", "Canario")
bird.make_sound()

campeon = Dog("Campeón", "Siberiano")
campeon.make_sound()