class Nodo:
    def __init__(self, valor, nivel=0):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.nivel = nivel


class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def crear_nodo(self, valor, nivel=0):
        return Nodo(valor, nivel=nivel)

    def crear_raiz(self, valor):
        if self.raiz:
            return self.raiz
        self.raiz = self.crear_nodo(valor)
        self.cantidad = 1
        return self.raiz

    def insertar(self, valor):
        if self.raiz is None:
            return self.crear_raiz(valor)

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

    def imprimir_preorden(self, nodo):
        if nodo is None:
            return
        print(f"{nodo.valor} (nivel {nodo.nivel})")
        self.imprimir_preorden(nodo.izquierdo)
        self.imprimir_preorden(nodo.derecho)

    def liberar_subarbol(self, nodo):
        if nodo is None:
            return
        self.liberar_subarbol(nodo.izquierdo)
        self.liberar_subarbol(nodo.derecho)
        nodo.izquierdo = None
        nodo.derecho = None

    def limpiar_arbol(self):
        self.liberar_subarbol(self.raiz)
        self.raiz = None
        self.cantidad = 0


if __name__ == "__main__":
    arbol = ArbolBinarioOrdenado()
    for valor in (10, 5, 20, 3, 7):
        arbol.insertar(valor)

    print("Recorrido preorden:")
    arbol.imprimir_preorden(arbol.raiz)

    arbol.limpiar_arbol()