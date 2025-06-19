#!/usr/bin/python3
"""
### **6. Contador de Palíndromos**

**Instrucción**:

Define una función `contar_palindromos(lista)` que cuente cuántas palabras en
una lista son palíndromos (se leen igual al revés). Ignora mayúsculas/minúsculas.

**Ejemplo**:

```python
contar_palindromos(["Radar", "Python", "reconocer"])  # Debe retornar 2

```
"""


def contar_palindromos(lista):
    contador = 0

    for palabra in lista:
        palabra = palabra.lower()

        if palabra == palabra[::-1]:
            contador += 1

    return contador

print(contar_palindromos(["Radar", "Python", "reconocer"]))  # Debe retornar 2
print(contar_palindromos(["oso", "casa", "Ana", "Python"]))  # Debe retornar 2
print(contar_palindromos(["amor", "Roma", "comer"]))        # Debe retornar 0