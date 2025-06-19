class Estudiante:
    def __init__(self, nombre: str, calificaciones: list = None):
        self.nombre = nombre
        self.calificaciones = calificaciones if calificaciones is not None else []
    
    def agregar_calificacion(self, nota: float):
        self.calificaciones.append(nota)
    
    def promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def aprobado(self) -> bool:
        return self.promedio() >= 6.0

# Ejemplo de uso
est = Estudiante("Luis")
est.agregar_calificacion(7.5)
est.agregar_calificacion(5.0)
print(est.promedio())   # 6.25
print(est.aprobado())   # True