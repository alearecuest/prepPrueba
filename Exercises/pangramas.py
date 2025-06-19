"""
Crea una función es_pangrama(frase) que determine si una frase es un pangrama (contiene todas las letras del alfabeto español).
Ignora mayúsculas/minúsculas y caracteres no alfabéticos.
"""
def es_pangrama(frase):
    frase = frase.lower()
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    
    for letra in alfabeto:
        if letra not in frase:
            return False
    return True

print(es_pangrama("Lo que pasa es que no es pangrama"))