class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.sig = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_inicio(self, valor):
        nuevo = NodoDoble(valor)
        nuevo.sig = self.cabeza
        if self.cabeza:
            self.cabeza.ant = nuevo
        else:
            self.cola = nuevo
        self.cabeza = nuevo

    def insertar_final(self, valor):
        nuevo = NodoDoble(valor)
        if self.cola is None:
            self.cabeza = self.cola = nuevo
            return
        nuevo.ant = self.cola
        self.cola.sig = nuevo
        self.cola = nuevo

    def eliminar_nodo(self, nodo):
        if nodo is None:
            return
        if nodo.ant:
            nodo.ant.sig = nodo.sig
        else:
            self.cabeza = nodo.sig
        if nodo.sig:
            nodo.sig.ant = nodo.ant
        else:
            self.cola = nodo.ant
        nodo.ant = nodo.sig = None

    def imprimir(self):
        reco = self.cabeza
        while reco:
            print(reco.valor, end=" -> ")
            reco = reco.sig
        print("None")

    def imprimir_inverso(self):
        reco = self.cola
        while reco:
            print(reco.valor, end=" <- ")
            reco = reco.ant
        print("None")

    def limpiar(self):
        while self.cabeza:
            siguiente = self.cabeza.sig
            self.cabeza.ant = None
            self.cabeza.sig = None
            self.cabeza = siguiente
        self.cola = None


def main():
    lista = ListaDoble()
    lista.insertar_inicio(10)
    lista.insertar_final(20)
    lista.insertar_inicio(5)
    print("Recorrido adelante:")
    lista.imprimir()
    print("Recorrido inverso:")
    lista.imprimir_inverso()
    # Eliminar el nodo intermedio (valor 10)
    lista.eliminar_nodo(lista.cabeza.sig)
    print("Tras eliminar el nodo central:")
    lista.imprimir()
    lista.limpiar()


if __name__ == "__main__":
    main()