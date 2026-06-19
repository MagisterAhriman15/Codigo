import csv

class Videojuego:
    def __init__(self, titulo, precio, stock):
        self.titulo = titulo
        self.precio = precio
        self.stock = stock

# 1. CÓMO ESCRIBIR (Guardar en el CSV)
def guardar_juegos_csv(lista_juegos, nombre_archivo):
    # 'w' es el modo de escritura (write). Si el archivo no existe, lo crea.
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        # Definimos los nombres de las columnas (deben coincidir con tus atributos)
        campos = ['titulo', 'precio', 'stock']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        
        escritor.writeheader() # Escribe la primera fila con los nombres de las columnas
        
        for juego in lista_juegos:
            # Escribimos cada objeto convirtiendo sus atributos a un diccionario
            escritor.writerow({
                'titulo': juego.titulo,
                'precio': juego.precio,
                'stock': juego.stock
            })

# 2. CÓMO LEER (Cargar desde el CSV)
def cargar_juegos_csv(nombre_archivo):
    juegos_cargados = []
    # 'r' es el modo de lectura (read).
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            # Reconstruimos los objetos instanciando la clase nuevamente
            # Nota: CSV guarda todo como texto, hay que convertir números de vuelta a int/float
            nuevo_juego = Videojuego(
                titulo=fila['titulo'], 
                precio=float(fila['precio']), 
                stock=int(fila['stock'])
            )
            juegos_cargados.append(nuevo_juego)
            
    return juegos_cargados

# --- Uso del ejemplo ---
# Mis datos iniciales
catalogo = [
    Videojuego("The Witcher 3", 29.99, 15),
    Videojuego("Hollow Knight", 14.99, 40)
]

# Guardamos los datos
guardar_juegos_csv(catalogo, 'inventario_juegos.csv')

# Los leemos en una nueva lista
juegos_recuperados = cargar_juegos_csv('inventario_juegos.csv')

for j in juegos_recuperados:
    print(f"Recuperado: {j.titulo} - Quedan {j.stock} unidades.")