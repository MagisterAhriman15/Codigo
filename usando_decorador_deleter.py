class Persona:
    def __init__(self, nombre):
        self.__nombre=nombre
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.deleter
    def nombre(self):
        print("Eliminando nombre")
        del self.__nombre

p=Persona("Luis")
print(p.nombre)
del p.nombre
        