"""
Define una clase abstracta **`FiguraGeometrica`** con método abstracto **`area()`**.

Implementa subclases **`Circulo`** y **`Triangulo`** que calculen su área.
"""
from abc import ABC, abstractmethod
from math import pi

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return pi * (self.radio ** 2)

class Triangulo (FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base * self.altura) /2
        