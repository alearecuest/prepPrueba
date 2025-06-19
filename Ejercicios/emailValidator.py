#!/usr/bin/python3
"""
### **7. Validador de Correos Electrónicos**

**Instrucción**:

Escribe una función `email_valido(email)` que verifique si un email cumple:

- Tiene un solo `@`.
- Dominio después de `@` es "[gmail.com](http://gmail.com/)",
"[hotmail.com](http://hotmail.com/)" o "[outlook.es](http://outlook.es/)".
- No contiene espacios.**Ejemplo**:

```python
email_valido("usuario@outlook.es")   # True
email_valido("inválido@yahoo.com")   # False

```
"""


def email_valido(email):
    if ' ' in email:
        return False
    
    if email.count('@') != 1:
        return False

    partes = email.split('@')
    dominio = partes[1]

    dominios_permitidos = ["gmail.com", "hotmail.com", "outlook.es"]
    if dominio not in dominios_permitidos:
        return False

    return True

print(email_valido("usuario@outlook.es"))   # True (cumple todos los criterios)
print(email_valido("inválido@yahoo.com"))   # False (dominio no permitido)
print(email_valido("usuario@gmail.com"))    # True (cumple todos los criterios)
print(email_valido("usuario con espacio@hotmail.com"))  # False (contiene espacio)
print(email_valido("sin-arroba.com"))       # False (no tiene @)
print(email_valido("doble@@gmail.com"))     # False (tiene dos @)