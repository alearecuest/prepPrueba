"""
### **9. Encontrar el Número Solitario**

**Instrucción**:

Escribe una función `numero_solitario(lista)`
que retorne el número que aparece **una sola vez** en una lista donde todos los demás aparecen dos veces.
"""
def numero_solitario(lista):
    conteo = {}

    # Contar cuántas veces aparece cada número
    for numero in lista:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1

    # Buscar el número que aparece una sola vez
    for numero, cantidad in conteo.items():
        if cantidad == 1:
            return numero



print(numero_solitario([4, 2, 3, 2, 4]))

"""
def numero_solitario(lista):
    resultado = 0
    for numero in lista:
        resultado ^= numero
    return resultado
"""