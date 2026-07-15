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

    def construir_desde_lista(self, valores, reiniciar=True):
        if reiniciar:
            self.limpiar_arbol()
        for valor in valores:
            self.insertar(valor)

    def _construir_balanceado_rec(self, valores, inicio, fin, nivel):
        if inicio > fin:
            return None
        medio = (inicio + fin) // 2
        nodo = self.crear_nodo(valores[medio], nivel=nivel)
        nodo.izquierdo = self._construir_balanceado_rec(valores, inicio, medio - 1, nivel + 1)
        nodo.derecho = self._construir_balanceado_rec(valores, medio + 1, fin, nivel + 1)
        self.cantidad += 1
        return nodo

    def construir_balanceado(self, valores):
        self.limpiar_arbol()
        if not valores:
            return True
        self.cantidad = 0
        self.raiz = self._construir_balanceado_rec(valores, 0, len(valores) - 1, 0)
        return self.raiz is not None

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


def imprimir_inorden(nodo):
    if nodo is None:
        return
    imprimir_inorden(nodo.izquierdo)
    print(nodo.valor, end=" ")
    imprimir_inorden(nodo.derecho)


if __name__ == "__main__":
    arbol = ArbolBinarioOrdenado()

    datos = [10, 5, 20, 3, 7, 15]
    arbol.construir_desde_lista(datos)

    print("Arbol generado con inserciones secuenciales:")
    arbol.imprimir_preorden(arbol.raiz)
    print("Inorden:")
    imprimir_inorden(arbol.raiz)
    print()

    ordenados = [2, 4, 6, 8, 12, 16, 18]
    if arbol.construir_balanceado(ordenados):
        print("\nArbol balanceado:")
        arbol.imprimir_preorden(arbol.raiz)
        print("Inorden:")
        imprimir_inorden(arbol.raiz)
        print()
    else:
        print("No se pudo construir el arbol balanceado.")

    arbol.limpiar_arbol()