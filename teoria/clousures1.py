def creador_saludo(idioma):
    if idioma == "es":
        prefijo = "¡Hola"
    elif idioma == "en":
        prefijo = "Hello"
    else:
        prefijo = "Saludos"

    def generar_saludo(nombre): # Funcion anidada
        # 'prefijo' y 'nombre' son del ámbito encerrador y local, respectivamente
        return f"{prefijo}, {nombre}!" # Accede a 'prefijo' del ámbito E
    
    return generar_saludo # ¡Devolvemos la función anidada!

# Creamos una función anidada configurada para español
saludar_espanol = creador_saludo("es") 
# La función 'creador_saludo' ya terminó de ejecutarse,
# pero 'saludar_espanol' (la función interna) "recuerda" que 'prefijo' era "¡Hola"

print(saludar_espanol("Maria")) # Salida: ¡Hola, Maria!

# Creamos otra función anidada configurada para inglés
saludar_ingles = creador_saludo("en")
print(saludar_ingles("John")) # Salida: Hello, John!