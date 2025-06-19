"""
3. **Polimorfismo**
    
    Crea una clase base **`Animal`** con método **`sonido()`**.
    
    Implementa subclases **`Perro`** y **`Gato`** que sobrescriban **`sonido()`** con sus respectivos sonidos.
"""
class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("woof!") 

class  Gato(Animal):
    def sonido(self):
        print("miau")
        