"""
Crea una clase **`Vehiculo`** con atributos **`marca`** y **`modelo`**.

Luego crea una clase **`Coche`** que herede de **`Vehiculo`** y añada el atributo **`num_puertas`**.
"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
        
auto = Coche("Fiat", "Argo", 4)