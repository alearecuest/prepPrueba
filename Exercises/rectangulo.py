"""
### **4. Clase "Rectángulo" con Herencia (POO)**

**Instrucción**:

Crea una clase `Rectangulo`:

- Atributos: `base`, `altura`.
- Métodos: `area()`, `perimetro()`.
Luego crea una clase `Cuadrado` que herede de `Rectangulo` y simplifique la inicialización (solo un lado).**Ejemplo**:
"""
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (2 * (self.base + self.altura))

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

rect = Rectangulo(3, 4)
print(rect.area())       # 12
cuad = Cuadrado(5)
print(cuad.perimetro())  # 20
