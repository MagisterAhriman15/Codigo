class Nodo:
    def __init__(self, valor, nivel=0):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.nivel = nivel


class ArbolBusqueda:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def crear_nodo(self, valor, nivel=0):
        return Nodo(valor, nivel=nivel)

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = self.crear_nodo(valor)
            self.cantidad = 1
            return self.raiz
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = self.crear_nodo(valor, nivel=actual.nivel + 1)
                    self.cantidad += 1
                    return actual.izquierdo
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = self.crear_nodo(valor, nivel=actual.nivel + 1)
                    self.cantidad += 1
                    return actual.derecho
                actual = actual.derecho

    def buscar(self, valor):
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return actual
            actual = actual.izquierdo if valor < actual.valor else actual.derecho
        return None

    def minimo(self, nodo):
        if nodo is None:
            return None
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

    def eliminar(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierdo = self.eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self.eliminar(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            sucesor = self.minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self.eliminar(nodo.derecho, sucesor.valor)
        return nodo

    def imprimir_inorden(self, nodo):
        if nodo is None:
            return
        self.imprimir_inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        self.imprimir_inorden(nodo.derecho)

    def limpiar(self, nodo):
        if nodo is None:
            return
        self.limpiar(nodo.izquierdo)
        self.limpiar(nodo.derecho)
        nodo.izquierdo = None
        nodo.derecho = None


if __name__ == "__main__":
    abb = ArbolBusqueda()
    for valor in [15, 8, 20, 4, 10, 17, 25]:
        abb.insertar(valor)

    print("Inorden:")
    abb.imprimir_inorden(abb.raiz)

    objetivo = 10
    encontrado = abb.buscar(objetivo)
    print(f"\nBuscar {objetivo}: {'hallado' if encontrado else 'no encontrado'}")

    abb.raiz = abb.eliminar(abb.raiz, 15)
    print("Inorden tras eliminar la raiz:")
    abb.imprimir_inorden(abb.raiz)
    print()

    abb.limpiar(abb.raiz)
    abb.raiz = None
    abb.cantidad = 0
