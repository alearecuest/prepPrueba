#!/usr/bin/env python3
"""
### **1. Secuencia de Collatz**

**Instrucción**:

Escribe una función `collatz(n)` que reciba un entero positivo
`n` y devuelva **el número de pasos** necesarios para llegar
a 1 aplicando estas reglas:

- Si `n` es par: divídelo entre 2.
- Si `n` es impar: multiplícalo por 3 y súmale 1.**Ejemplo**:

```python
collatz(6)  # Debe retornar 8 
(porque: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1)

```
"""


def collatz(n):
    if n <= 0:
        raise ValueError("The number must be a postive integer")
    
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps

if __name__ == "__main__":
    try:
        num = int(input("Introduce un número entero positivo: "))
        result = collatz(num)
        print(f"El número de pasos para llegar a 1 es: {result}")
    except ValueError as e:
        print(f"Error: {e}")
