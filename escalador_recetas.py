"""
nombre_ingrediente es un string
cantidad es un int
existencia es un bool, True es Si, False es No
"""

import csv

class Ingrediente():
    def __init__(self, nombre_ingrediente, cantidad, unidad_medida, existencia):
        self.nombre_ingrediente:str=nombre_ingrediente
        self.cantidad:int=cantidad
        self.unidad_medida:str=unidad_medida
        self.existencia:bool=existencia
        
    def imprimir(self):
        return print(self.nombre_ingrediente, self.cantidad, self.unidad_medida, self.existencia)
    
    def aumentarCantidad(self, aumentar):
        pass
    
    def disminuirCantidad(self, disminuir):
        pass
    

def guardar_ingredientes_csv(lista_ingredientes, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['nombre_ingrediente', 'cantidad', 'unidad_medida', 'existencia']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader() 
        for ingrediente in lista_ingredientes:
            # Escribimos cada objeto convirtiendo sus atributos a un diccionario
            escritor.writerow({
                'nombre_ingrediente': ingrediente.nombre_ingrediente,
                'cantidad': ingrediente.cantidad,
                'unidad_medida': ingrediente.unidad_medida,
                'existencia': ingrediente.existencia,
            })
    
def cargar_ingredientes_csv(nombre_archivo):
    ingredientes_cargados = []
    # 'r' es el modo de lectura (read).
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)        
        for fila in lector:
            nuevo_ingrediente = Ingrediente(
                nombre_ingrediente=fila['nombre_ingrediente'], 
                cantidad=int(fila['cantidad']), 
                unidad_medida=fila['unidad_medida'],
                existencia=bool(fila['existencia'])
            )
            ingredientes_cargados.append(nuevo_ingrediente)
    return ingredientes_cargados
    
catalogo_ingredientes = [
    Ingrediente("pasta", 20, "kg", True),
    Ingrediente("dientes de ajo", 5, "cabezas", True),
    Ingrediente("aceite de oliva", 5, "bolsas", True),
    Ingrediente("carne", 2, "kg", True)
]

# Guardamos los datos
guardar_ingredientes_csv(catalogo_ingredientes, 'inventario_ingredientes.csv')

# Los leemos en una nueva lista
ingredientes_recuperados = cargar_ingredientes_csv('inventario_ingredientes.csv')

print("Bienvenido al escalador de recetas")

for j in ingredientes_recuperados:
    print(f"Recuperado: {j.nombre_ingrediente} - Quedan {j.cantidad} {j.unidad_medida}.")

instrucciones_cocina = """
Instrucciones de cocina
Paso 1: Hierve agua en una olla grande
Paso 2: Agrega 1 kg de pasta y cocina durante 10 minutos
Paso 3: Prepare la salsa en una sarten, use 1 kg de carne, 1 cabeza de ajo y 2 bolsas de aceite de oliva
Paso 4: Cuele la pasta del agua, cuando enfrie, combinarlo con la salsa y ya estaria
"""

print(instrucciones_cocina)

"""
Posibles cambios
-ver que hacer con instrucciones de cocina, no se si otra clase o que con un metodo haga las modificaciones de cantidad, añadir de otros
platos, se debe cambiar en los csv.
-Puedo usar un bucle while para generar un menú, junto a user input para las entradas de usuario
"""
