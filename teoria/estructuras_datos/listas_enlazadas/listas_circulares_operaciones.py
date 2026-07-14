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

    def eliminar(self, valor):
        if self.cola is None:
            return False
        reco = self.cola.sig
        ant = self.cola
        while True:
            if reco.valor == valor:
                if reco == ant:
                    self.cola = None
                else:
                    ant.sig = reco.sig
                    if reco == self.cola:
                        self.cola = ant
                reco.sig = None
                return True
            ant = reco
            reco = reco.sig
            if reco == self.cola.sig:
                break
        return False

    def imprimir(self):
        if self.cola is None:
            print("(lista vacia)")
            return
        inicio = self.cola.sig
        reco = inicio
        while True:
            print(reco.valor, end=" -> ")
            reco = reco.sig
            if reco == inicio:
                break
        print("(inicio)")

    def limpiar(self):
        if self.cola is None:
            return
        inicio = self.cola.sig
        reco = inicio
        while True:
            siguiente = reco.sig
            reco.sig = None
            if siguiente == inicio:
                break
            reco = siguiente
        self.cola = None


def main():
    lista = ListaCircular()
    for v in (5, 10, 15):
        lista.insertar(v)
    print("Lista circular:")
    lista.imprimir()
    lista.eliminar(10)
    print("Tras eliminar 10:")
    lista.imprimir()
    lista.limpiar()


if __name__ == "__main__":
    main()