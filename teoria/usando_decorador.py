class Circulo:
    def __init__(self, radio):
        self.__radio=radio
    
    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, valor):
        if valor<0:
            raise ValueError
        self.radio=valor

c=Circulo(5)
print(c.radio)