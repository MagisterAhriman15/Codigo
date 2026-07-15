from collections import deque


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return self.raiz

        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(valor)
                    return actual.izquierdo
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = Nodo(valor)
                    return actual.derecho
                actual = actual.derecho

    def altura(self, nodo=None):
        def _altura(n):
            if n is None:
                return -1
            return 1 + max(_altura(n.izquierdo), _altura(n.derecho))

        nodo = self.raiz if nodo is None else nodo
        return _altura(nodo)

    def contar_nodos(self, nodo=None):
        def _contar(n):
            if n is None:
                return 0
            return 1 + _contar(n.izquierdo) + _contar(n.derecho)

        nodo = self.raiz if nodo is None else nodo
        return _contar(nodo)

    def contar_hojas(self, nodo=None):
        def _contar_hojas(n):
            if n is None:
                return 0
            if n.izquierdo is None and n.derecho is None:
                return 1
            return _contar_hojas(n.izquierdo) + _contar_hojas(n.derecho)

        nodo = self.raiz if nodo is None else nodo
        return _contar_hojas(nodo)

    def contar_internos(self, nodo=None):
        def _contar_internos(n):
            if n is None or (n.izquierdo is None and n.derecho is None):
                return 0
            return 1 + _contar_internos(n.izquierdo) + _contar_internos(n.derecho)

        nodo = self.raiz if nodo is None else nodo
        return _contar_internos(nodo)

    def factor_balance(self, nodo=None):
        nodo = self.raiz if nodo is None else nodo
        if nodo is None:
            return 0
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)

    def ancho_maximo(self):
        if self.raiz is None:
            return 0

        cola = deque([self.raiz])
        max_ancho = 0

        while cola:
            nivel_actual = len(cola)
            max_ancho = max(max_ancho, nivel_actual)
            for _ in range(nivel_actual):
                nodo = cola.popleft()
                if nodo.izquierdo:
                    cola.append(nodo.izquierdo)
                if nodo.derecho:
                    cola.append(nodo.derecho)
        return max_ancho

    def profundidad_de_valor(self, valor):
        nivel = 0
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return nivel
            nivel += 1
            actual = actual.izquierdo if valor < actual.valor else actual.derecho
        return -1


if __name__ == "__main__":
    arbol = ArbolBinarioOrdenado()
    for valor in [10, 5, 15, 3, 7, 12, 18]:
        arbol.insertar(valor)

    print(f"Altura: {arbol.altura()}")
    print(f"Cantidad de nodos: {arbol.contar_nodos()}")
    print(f"Cantidad de hojas: {arbol.contar_hojas()}")
    print(f"Nodos internos: {arbol.contar_internos()}")
    print(f"Ancho maximo: {arbol.ancho_maximo()}")

    buscado = 7
    profundidad = arbol.profundidad_de_valor(buscado)
    print(f"Profundidad de {buscado}: {profundidad}")