class NodoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class ListaCircular:
    def __init__(self):
        self.cola = None  # cola.sig apunta al primer nodo

    def insertar(self, valor):
        nuevo = NodoCircular(valor)
        if self.cola is None:
            nuevo.sig = nuevo
            self.cola = nuevo
            return
        nuevo.sig = self.cola.sig
        self.cola.sig = nuevo
        self.cola = nuevo

    def recorrer(self):
        if self.cola is None:
            return
        inicio = self.cola.sig
        reco = inicio
        while True:
            print(reco.valor, end=" ")
            reco = reco.sig
            if reco is inicio:
                break
        print()