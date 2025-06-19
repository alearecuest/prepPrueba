"""
### **7. Validador de Correos Electrónicos**

**Instrucción**:

Escribe una función `email_valido(email)` que verifique si un email cumple:

- Tiene un solo `@`.
- Dominio después de `@` es "[gmail.com](http://gmail.com/)", "[hotmail.com](http://hotmail.com/)" o "[outlook.es](http://outlook.es/)".
- No contiene espacios.
"""
def email_valido(email):
    while email:
        if " " in email:
            return False, f"Tu {email} tiene espacios no funciona"
    
        if email.count("@") == 1:
           partes = email.split("@")
           dominio = partes[1]
           if dominio in ["gmail.com", "hotmail.com", "outlook.es"]:
               return True
           else:
               return False, f"ese no es un dominio válido"

print(email_valido(email = "emanuel@gmal.com"))
