#!/usr/bin/python3
"""
### **9. Encontrar el Número Solitario**

**Instrucción**:

Escribe una función `numero_solitario(lista)` que retorne el número que aparece
**una sola vez** en una lista donde todos los demás aparecen dos veces.

**Ejemplo**:

```python
numero_solitario([4, 2, 3, 2, 4])  # Debe retornar 3

```
"""


def numero_solitario(lista):
    contador = {}

    for num in lista:
        if num is contador:
            contador[num] += 1
        else:
            contador[num] = 1

    for num, cantidad in contador.items():
        if cantidad == 1:
            return num

# Código para probar la función
if __name__ == "__main__":
    # Ejemplo del enunciado
    print(numero_solitario([4, 2, 3, 2, 4]))  # Debe retornar 3
    
    # Pruebas adicionales
    print(numero_solitario([1, 1, 2, 2, 3]))  # Debe retornar 3
    print(numero_solitario([7, 5, 5, 7, 9]))  # Debe retornar 9