class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.sig = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_final(self, valor):
        nuevo = NodoDoble(valor)
        if self.cola is None:
            self.cabeza = self.cola = nuevo
            return
        nuevo.ant = self.cola
        self.cola.sig = nuevo
        self.cola = nuevo