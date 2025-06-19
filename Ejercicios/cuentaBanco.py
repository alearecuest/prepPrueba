#!/usr/bin/python3
"""
### **3. Clase "CuentaBancaria" (POO)**

**Instrucción**:

Implementa una clase `CuentaBancaria` con:

- Atributos: `titular` (str), `saldo` (float).
- Métodos:
    - `depositar(monto)`: añade `monto` al saldo.
    - `retirar(monto)`: resta `monto` si hay saldo suficiente;
    si no, imprime "Fondos insuficientes".
    - `__str__()`: retorna "Cuenta de {titular}: ${saldo}".**Ejemplo**:

```python
cuenta = CuentaBancaria("Ana", 1000)
cuenta.retirar(500)  # Saldo restante: 500
print(cuenta)        # "Cuenta de Ana: $500.0"

```
"""


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
        else:
            print("Fondos insuficiente")
    
    def __str__(self):
        return f"La cuenta de: {self.titular} tiene saldo: {self.saldo}"

cuenta = CuentaBancaria("Ana", 1000)
cuenta.retirar(500)  # Saldo restante: 500
print(cuenta)        # "Cuenta de Ana: $500.0"