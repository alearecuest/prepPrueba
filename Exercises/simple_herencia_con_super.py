"""
Crea una clase Empleado con atributos nombre y salario.
Deriva una clase Gerente que añada departamento y use super() en su constructor.
"""
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nDepartamento: {self.departamento}"

empleado = Gerente("Emanuel", "$200.000", "CIBER-SEGURIDAD")
print(empleado)
