"""
### **8. Clase "Libro" con Método Estático (POO)**

**Instrucción**:

Crea una clase `Libro`:

- Atributos: `titulo`, `autor`, `año_publicacion`.
- Método estático: `es_antiguo(año)` retorna `True` si el año es < 1900.
- Método de instancia: `info()` retorna "Título: {titulo}, Autor: {autor}".**Ejemplo**:
"""
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    def info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
        
    @staticmethod
    def es_antiguo(año):
        if año < 1900:
            return True

libro = Libro("Biblia", "Dios", 0)
print(libro.info())
print(libro.es_antiguo(0))