class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def imprimir(self):
        reco = self.cabeza
        while reco:
            print(reco.valor, end=" -> ")
            reco = reco.sig
        print("None")

    def limpiar(self):
        while self.cabeza:
            siguiente = self.cabeza.sig
            self.cabeza.sig = None
            self.cabeza = siguiente


def main():
    lista = ListaEnlazada()

    for valor in (30, 20, 10):
        lista.insertar_inicio(valor)

    print("Lista actual:")
    lista.imprimir()

    lista.limpiar()


if __name__ == "__main__":
    main()