"""
Define una función contar_palindromos(lista) 
que cuente cuántas palabras en una lista son palíndromos (se leen igual al revés).
Ignora mayúsculas/minúsculas.
"""
def is_palindromo(palabra):
    palabra = palabra.lower()
    palabra_reves = palabra[::-1]
    if palabra_reves == palabra:
        return True
    else:
        return False
    
def contar_palindromos(lista:list):
    
    count = 0
    for n in lista:
        if is_palindromo(n):
            count += 1
    return (count)

probando = ["oso", "Peñarol", "casa"]
print(f" Ahora sabremos cuantos palindromos hay: {contar_palindromos(probando)}")