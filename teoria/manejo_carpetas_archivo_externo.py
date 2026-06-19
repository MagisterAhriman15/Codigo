import os

# 1. Definimos los nombres
carpeta_destino = "archivos_texto"
nombre_archivo = "registro_ejemplo.txt"

# 2. Nos aseguramos de que la carpeta exista en el sistema
# Si la carpeta 'archivos_texto' no existe, la crea. Si ya existe, sigue adelante.
os.makedirs(carpeta_destino, exist_ok=True)

# 3. Unimos la carpeta y el archivo de forma segura
ruta_segura = os.path.join(carpeta_destino, nombre_archivo)

print(f"La ruta generada es: {ruta_segura}")
# Salida en Windows: archivos_texto\registro_ejemplo.txt
# Salida en Mac/Linux: archivos_texto/registro_ejemplo.txt

# 4. Ahora puedes usar esa ruta para guardar o leer
# funcion_guardar(datos, ruta_segura)