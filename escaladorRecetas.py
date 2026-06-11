"""
nombre_ingrediente es un string
cantidad es un int
existencia es un bool, True es Si, False es No
"""

class Ingrediente():
    def __init__(self, nombre_ingrediente, cantidad, unidad_medida, existencia):
        self.nombre_ingrediente:str=nombre_ingrediente
        self.cantidad:int=cantidad
        self.unidad_medida:str=unidad_medida
        self.existencia:bool=existencia
        
    def imprimir(self):
        return print(self.nombre_ingrediente, self.cantidad, self.unidad_medida, self.existencia)
        
    
        

print("Bienvenido al escalador de recetas")
ingredientes={"pasta":20, "dientes de ajo":5, "aceite de oliva":5, "carne":2}
ingredientes_nombre=ingredientes.keys()
ingredientes_cantidad=ingredientes.values()
ingredientes_pares=ingredientes.items()
ingrediente1=Ingrediente("pasta", 20, "kg", True)
ingrediente2=Ingrediente("dientes de ajo", 5, "cabezas", True)
ingrediente3=Ingrediente("aceite de oliva", 5, "bolsas", True)
ingrediente4=Ingrediente("carne", 2, "kg", True)
ingrediente1.imprimir()
ingrediente2.imprimir()
ingrediente3.imprimir()
ingrediente4.imprimir()


instrucciones_cocina = """
Instrucciones de cocina
Paso 1: Hierve agua en una olla grande
Paso 2: Agrega 1 kg de pasta y cocina durante 10 minutos
Paso 3: Prepare la salsa en una sarten, use 1 kg de carne, 1 cabeza de ajo y 2 bolsas de aceite de oliva
Paso 4: Cuele la pasta del agua, cuando enfrie, combinarlo con la salsa y ya estaria
"""

print(instrucciones_cocina)
