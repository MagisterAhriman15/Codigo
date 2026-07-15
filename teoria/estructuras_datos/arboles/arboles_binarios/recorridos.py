from collections import deque


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

    def imprimir_preorden(self, nodo):
        if nodo is None:
            return
        print(f"{nodo.valor} (nivel {nodo.nivel})")
        self.imprimir_preorden(nodo.izquierdo)
        self.imprimir_preorden(nodo.derecho)

    def imprimir_inorden(self, nodo):
        if nodo is None:
            return
        self.imprimir_inorden(nodo.izquierdo)
        print(f"{nodo.valor} (nivel {nodo.nivel})")
        self.imprimir_inorden(nodo.derecho)

    def imprimir_postorden(self, nodo):
        if nodo is None:
            return
        self.imprimir_postorden(nodo.izquierdo)
        self.imprimir_postorden(nodo.derecho)
        print(f"{nodo.valor} (nivel {nodo.nivel})")

    def imprimir_preorden_iterativo(self, nodo):
        if nodo is None:
            return
        pila = [nodo]
        while pila:
            actual = pila.pop()
            print(f"{actual.valor} (nivel {actual.nivel})")
            if actual.derecho:
                pila.append(actual.derecho)
            if actual.izquierdo:
                pila.append(actual.izquierdo)

    def imprimir_por_niveles(self, nodo):
        if nodo is None:
            return
        cola = deque([nodo])
        while cola:
            actual = cola.popleft()
            print(f"{actual.valor} (nivel {actual.nivel})")
            if actual.izquierdo:
                cola.append(actual.izquierdo)
            if actual.derecho:
                cola.append(actual.derecho)

    def limpiar_arbol(self):
        self._limpiar(self.raiz)
        self.raiz = None
        self.cantidad = 0

    def _limpiar(self, nodo):
        if nodo is None:
            return
        self._limpiar(nodo.izquierdo)
        self._limpiar(nodo.derecho)
        nodo.izquierdo = None
        nodo.derecho = None


if __name__ == "__main__":
    arbol = ArbolBinarioOrdenado()
    valores = [10, 5, 15, 3, 7, 12, 18]
    for valor in valores:
        arbol.insertar(valor)

    print("Preorden:")
    arbol.imprimir_preorden(arbol.raiz)

    print("\nInorden:")
    arbol.imprimir_inorden(arbol.raiz)

    print("\nPostorden:")
    arbol.imprimir_postorden(arbol.raiz)

    print("\nPreorden iterativo:")
    arbol.imprimir_preorden_iterativo(arbol.raiz)

    print("\nRecorrido por niveles:")
    arbol.imprimir_por_niveles(arbol.raiz)

    arbol.limpiar_arbol()