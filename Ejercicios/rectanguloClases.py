#!/usr/bin/python3
"""
### **4. Clase "Rectángulo" con Herencia (POO)**

**Instrucción**:

Crea una clase `Rectangulo`:

- Atributos: `largo`, `ancho`.
- Métodos: `area()`, `perimetro()`.
Luego crea una clase `Cuadrado` que herede de `Rectangulo` y simplifique
la inicialización (solo un lado).**Ejemplo**:

```python
rect = Rectangulo(3, 4)
rect.area()       # 12
cuad = Cuadrado(5)
cuad.perimetro()  # 20

```
"""


class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        return (self.largo * self.ancho)
    
    def perimetro(self):
        return 2 * (self.largo + self.ancho)

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

rect = Rectangulo(3, 4)
rect.area()
cuad = Cuadrado(5)
cuad.perimetro()
print(f"Área del rectángulo: {rect.area()}")
print(f"Perímetro del rectángulo: {rect.perimetro()}")