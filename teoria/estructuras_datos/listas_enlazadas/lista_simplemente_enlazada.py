class NodoSimple:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo = NodoSimple(valor)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def imprimir(self):
        reco = self.cabeza
        while reco:
            print(reco.valor, end=" -> ")
            reco = reco.sig
        print("None")