#!/usr/bin/env python3
### **2. Verificador de Pangramas**
"""
**Instrucción**:

Crea una función `es_pangrama(frase)` que determine si una frase es un pangrama
(contiene todas las letras del alfabeto español). Ignora mayúsculas/minúsculas y
caracteres no alfabéticos.

**Ejemplo**:

```python
es_pangrama("El cadáver de Wamba, rey godo de España, fue exhumado y trasladado.") 
# Debe retornar True

```
"""

import unicodedata

def es_pangrama(frase):
    frase = frase.lower()

    alphabet = set("abcdefghijklmnñopqrstuvwxyz")
    found_letters = set()

    for character in frase:
        if character == 'ñ':
            found_letters.add('ñ')
        elif character in alphabet:
            found_letters.add(character)
        else:
            normalize = unicodedata.normalize('NFD', character)
            no_accent = ''.join(c for c in normalize if unicodedata.category(c) != 'Mn')
            for c in no_accent:
                if c in alphabet:
                    found_letters.add(c)
            
    return alphabet.issubset(found_letters)

# Código para probar la función
if __name__ == "__main__":

    ejemplos = [
        "El cadáver de Wamba, rey godo de España, fue exhumado y trasladado.",
        "Hola mundo",
        "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja."
    ]
    
    for i, frase in enumerate(ejemplos, 1):
        resultado = es_pangrama(frase)
        print(f"Ejemplo {i}: {frase}")
        print(f"¿Es pangrama? {'Sí' if resultado else 'No'}")
        print("-" * 50)
    

    print("Ingresa una frase para comprobar si es un pangrama:")
    frase_usuario = input("> ")
    resultado = es_pangrama(frase_usuario)
    print(f"¿Es pangrama? {'Sí' if resultado else 'No'}")
