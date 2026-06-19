"""
nombre_ingrediente es un string
cantidad es un int
existencia es un bool, True es Si, False es No
"""

import csv
import os

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
            escritor.writerow({
                'nombre_ingrediente': ingrediente.nombre_ingrediente,
                'cantidad': ingrediente.cantidad,
                'unidad_medida': ingrediente.unidad_medida,
                'existencia': ingrediente.existencia,
            })
    
def cargar_ingredientes_csv(nombre_archivo):
    ingredientes_cargados = []
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

def limpiar_consola():
    # 'nt' corresponde a Windows
    if os.name == 'nt':
        os.system('cls')
    # Para macOS y Linux (posix)
    else:
        os.system('clear')

carpeta_destino = "csv"
os.makedirs(carpeta_destino, exist_ok=True)
ruta_csv = os.path.join(carpeta_destino, 'inventario_ingredientes.csv')

guardar_ingredientes_csv(catalogo_ingredientes, ruta_csv)
ingredientes_recuperados = cargar_ingredientes_csv(ruta_csv)

instrucciones_cocina = """
Instrucciones de cocina
Paso 1: Hierve agua en una olla grande
Paso 2: Agrega 1 kg de pasta y cocina durante 10 minutos
Paso 3: Prepare la salsa en una sarten, use 1 kg de carne, 1 cabeza de ajo y 2 bolsas de aceite de oliva
Paso 4: Cuele la pasta del agua, cuando enfrie, combinarlo con la salsa y ya estaria
"""

flag=True

while(flag):
    limpiar_consola()
    print("Bienvenido al escalador de recetas")
    print("1. Ver inventario de ingredientes")
    print("2. Añadir ingredientes al inventario")
    print("3. Ver recetas")
    print("4. Indicar que receta se va a preparar, para modificar el inventario")
    print("0. Salir del programa")
    opcion_str=input("¿Que opcion deseas ejecutar? ")
    
    try:
        opcion=int(opcion_str)
    except ValueError:
        print("¡Error! Has introducido letras o caracteres inválidos. Debes escribir un número entero.")
        input("Presiona Enter para volver a intentarlo...")
        continue
    
    if opcion==1:
        for j in ingredientes_recuperados:
            print(f"Recuperado: {j.nombre_ingrediente} - Quedan {j.cantidad} {j.unidad_medida}.") 
        input("Presiona Enter para continuar...")
    elif opcion==2:
        pass
        #Añadir ingrediente
    elif opcion==3:
        print(instrucciones_cocina)
        input("Presiona Enter para continuar...")
    elif opcion==4:
        pass
        #Indicar receta a preparar
    elif opcion==0:
        break
    else:
        break

"""
Posibles cambios
-ver que hacer con instrucciones de cocina, no se si otra clase o que con un metodo haga las modificaciones de cantidad, añadir de otros
platos, se debe cambiar en los csv y en menu while loop.
-modificar la lectura del csv, porque luego los proyectos chicos tendran su propia carpeta y los csv tendran su otra carpeta, para que interactuen
"""
