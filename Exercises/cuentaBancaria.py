"""
**Instrucción**:
Implementa una clase `CuentaBancaria` con:

- Atributos: `titular` (str), `saldo` (float).
- Métodos:
    - `depositar(monto)`: añade `monto` al saldo.
    - `retirar(monto)`: resta `monto` si hay saldo suficiente; si no, imprime "Fondos insuficientes".
    - `__str__()`: retorna "Cuenta de {titular}: ${saldo}".**Ejemplo**:
"""
class CuentaBancaria:
    """Esta clase representa la cuenta de un banco"""
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if self.saldo > monto:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")
    
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.saldo}"

cuenta = CuentaBancaria("Ana", 1000)
cuenta.retirar(500)  # Saldo restante: 500
print(cuenta)        # "Cuenta de Ana: $500.0"

""" **Ejercicios de POO para Holberton**

1. **Encapsulación con Getters/Setters**
    
    Crea una clase **`CuentaBancaria2`**:
    
    - Atributo privado: **`_saldo`** (inicializado en 0)
    - Usa **`@property`** para el getter de **`saldo`**
    - Usa **`@saldo.setter`** para validar que el saldo no sea negativo
"""

class CuentaBancaria2:
    def __init__(self, saldo = 0):
        self._saldo = saldo
    
    @property
    def saldo(self):
        return self._saldo
        
    @saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            raise ValueError("saldo negativo")
        self._saldo = valor