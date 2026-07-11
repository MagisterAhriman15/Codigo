def validar_clave(clave):
    def tiene_minuscula():
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    def tiene_mayuscula():
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    def tiene_numero():
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False

    return tiene_minuscula() and tiene_mayuscula() and tiene_numero()


# --- Ejemplos de uso ---
print("--- Clave Válida ---")
clave1 = "MiClaveSegura123"
print(f"'{clave1}' es válida: {validar_clave(clave1)}") # Esperado: True
print("-" * 30)

print("\n--- Clave sin mayúscula ---")
clave2 = "miclavesegura123"
print(f"'{clave2}' es válida: {validar_clave(clave2)}") # Esperado: False
print("-" * 30)

print("\n--- Clave sin minúscula ---")
clave3 = "MICLAVESEGURA123"
print(f"'{clave3}' es válida: {validar_clave(clave3)}") # Esperado: False
print("-" * 30)

print("\n--- Clave sin número ---")
clave4 = "MiClaveSegura"
print(f"'{clave4}' es válida: {validar_clave(clave4)}") # Esperado: False
print("-" * 30)

print("\n--- Clave con solo minúsculas y números ---")
clave5 = "miclave123"
print(f"'{clave5}' es válida: {validar_clave(clave5)}") # Esperado: False
print("-" * 30)

print("\n--- Clave vacía ---")
clave6 = ""
print(f"'{clave6}' es válida: {validar_clave(clave6)}") # Esperado: False
print("-" * 30)
