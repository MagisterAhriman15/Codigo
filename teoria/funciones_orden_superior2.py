class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def es_mayor(self,fn):
        return fn(self.edad)

def mayor_estadosunidos(edad):
    if edad>=21:
        return True
    else:
        return False

def mayor_argentina(edad):
    if edad>=18:
        return True
    else:
        return False


persona1=Persona("juan", 18)
if persona1.es_mayor(mayor_argentina):
    print(f"{persona1.nombre} es mayor si vive en Argentina")
else:
    print(f"{persona1.nombre} no es mayor si vive en Argentina")
if persona1.es_mayor(mayor_estadosunidos):
    print(f"{persona1.nombre} es mayor si vive en Estados Unidos")
else:
    print(f"{persona1.nombre} no es mayor si vive en Estados Unidos")