#!/usr/bin/python3
"""
### **5. Gestor de Estudiantes (POO)**

**Instrucción**:

Crea una clase `Estudiante`:

- Atributos: `nombre` (str), `calificaciones` (lista de floats).
- Métodos:
    - `agregar_calificacion(nota)`: añade una nota a la lista.
    - `promedio()`: retorna el promedio de las notas.
    - `aprobado()`: retorna `True` si el promedio es ≥ 6.0.**Ejemplo**:

```python
est = Estudiante("Alejandro")
est.agregar_calificacion(7.5)
est.agregar_calificacion(5.0)
est.promedio()   # 6.25
est.aprobado()   # True

```
"""


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []
    
    def agregar_calificacion(self, nota):
        self.calificaciones.append(nota)
    
    def promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def aprobado(self):
        return self.promedio() >= 6.0

est = Estudiante("Alejandro")
est.agregar_calificacion(7.5)
est.agregar_calificacion(5.0)
est.promedio()
est.aprobado()

# Obtener el promedio
print(f"Promedio de {est.nombre}: {est.promedio()}")   # 6.25

# Verificar si aprobó
if est.aprobado():
    print(f"{est.nombre} ha aprobado.")
else:
    print(f"{est.nombre} no ha aprobado.")

# Agregar más calificaciones
est.agregar_calificacion(4.0)
print(f"Nuevo promedio: {est.promedio()}")  # (7.5 + 5.0 + 4.0) / 3 = 5.5
print(f"¿Aprobado? {est.aprobado()}")