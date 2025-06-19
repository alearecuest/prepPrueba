#!/usr/bin/python3
"""
### **10. Sistema de Figuras Geométricas (POO)**

**Instrucción**:

Implementa un sistema de figuras:

- Clase base `Figura` con método abstracto `area()`.
- Subclases `Circulo` (radio) y `Triangulo` (base, altura).
- Añade validación en `Triangulo`: si base o altura son ≤ 0, lanza `ValueError`.**Ejemplo**:

```python
circulo = Circulo(5)
circulo.area()  # ≈ 78.54 (5^2 * π)
triangulo = Triangulo(4, 3)
triangulo.area()  # 6.0

```
"""

from abc import ABC, abstractmethod
import math


class Figura:
    @abstractmethod
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        def area(self):
            return math.pi * self.radio ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero")
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
