"""
### **1. Secuencia de Collatz**
**Instrucción**:
Escribe una función `collatz(n)` que reciba un entero positivo
`n` y devuelva **el número de pasos** necesarios para llegar a 1 aplicando estas reglas:
- Si `n` es par: divídelo entre 2.
- Si `n` es impar: multiplícalo por 3 y súmale 1.**Ejemplo**:
"""
def collatz(n):
    count = 0
    while(n != 1):
        if n % 2 == 0:
            n = n // 2 
        else:
            n = n * 3 + 1
        count += 1
    return count

print(collatz(5))