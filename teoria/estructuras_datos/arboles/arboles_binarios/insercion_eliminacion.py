class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolABB:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def crear_nodo(self, valor):
        return Nodo(valor)

    def insertar_unico(self, valor):
        if self.raiz is None:
            self.raiz = self.crear_nodo(valor)
            self.cantidad = 1
            return self.raiz

        actual = self.raiz
        while True:
            if valor == actual.valor:
                return actual
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = self.crear_nodo(valor)
                    self.cantidad += 1
                    return actual.izquierdo
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = self.crear_nodo(valor)
                    self.cantidad += 1
                    return actual.derecho
                actual = actual.derecho

    def minimo(self, nodo=None):
        nodo = self.raiz if nodo is None else nodo
        while nodo and nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

    def eliminar(self, valor, nodo=None):
        nodo = self.raiz if nodo is None else nodo
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierdo = self.eliminar(valor, nodo.izquierdo)
        elif valor > nodo.valor:
            nodo.derecho = self.eliminar(valor, nodo.derecho)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            sucesor = self.minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self.eliminar(sucesor.valor, nodo.derecho)
        if nodo is self.raiz:
            self.raiz = nodo
        return nodo

    def buscar(self, valor):
        nodo = self.raiz
        while nodo:
            if valor == nodo.valor:
                return nodo
            nodo = nodo.izquierdo if valor < nodo.valor else nodo.derecho
        return None

    def remover_valor(self, valor):
        if not self.buscar(valor):
            return False
        self.raiz = self.eliminar(valor)
        if self.cantidad > 0:
            self.cantidad -= 1
        return True

    def imprimir_inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return
        self.imprimir_inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        self.imprimir_inorden(nodo.derecho)


if __name__ == "__main__":
    arbol = ArbolABB()
    for valor in [10, 4, 18, 2, 6, 15, 20]:
        arbol.insertar_unico(valor)

    print("Inorden inicial:")
    arbol.imprimir_inorden()
    print()

    arbol.raiz = eliminar(arbol.raiz, 2)
    print("Tras eliminar hoja 2:")
    arbol.imprimir_inorden()
    print()

    arbol.raiz = eliminar(arbol.raiz, 18)
    print("Tras eliminar nodo con un hijo (18):")
    arbol.imprimir_inorden()
    print()

    arbol.raiz = eliminar(arbol.raiz, 10)
    print("Tras eliminar la raiz (dos hijos):")
    arbol.imprimir_inorden()
    print()