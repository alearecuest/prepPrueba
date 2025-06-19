#!/usr/bin/python3
"""
### **8. Clase "Libro" con Método Estático (POO)**

**Instrucción**:

Crea una clase `Libro`:

- Atributos: `titulo`, `autor`, `año_publicacion`.
- Método estático: `es_antiguo(año)` retorna `True` si el año es < 1900.
- Método de instancia: `info()` retorna "Título: {titulo}, Autor: {autor}".**Ejemplo**:

```python
libro = Libro("Cien años de soledad", "García Márquez", 1967)
libro.es_antiguo(1850)  # True (llamada estática)
libro.info()            # "Título: Cien años de soledad, Autor: García Márquez"

```
"""


class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    @staticmethod
    def es_antiguo(año):
        return año < 1900

    def info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

# Crear una instancia de Libro
libro = Libro("Cien años de soledad", "García Márquez", 1967)

# Llamar al método estático (se puede llamar desde la instancia)
print(libro.es_antiguo(1850))  # True

# También se puede llamar directamente desde la clase
print(Libro.es_antiguo(1950))  # False

# Llamar al método de instancia
print(libro.info())  # "Título: Cien años de soledad, Autor: García Márquez"

# Verificar si el propio libro es antiguo
print(f"¿Es antiguo este libro? {Libro.es_antiguo(libro.año_publicacion)}")  # False (1967 > 1900)