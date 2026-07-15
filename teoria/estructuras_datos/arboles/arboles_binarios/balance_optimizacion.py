class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo=None):
        def _altura(n):
            if n is None:
                return 0
            return 1 + max(_altura(n.izquierdo), _altura(n.derecho))

        nodo = self.raiz if nodo is None else nodo
        return _altura(nodo)

    def factor_balance(self, nodo=None):
        nodo = self.raiz if nodo is None else nodo
        if nodo is None:
            return 0
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)

    def rotar_derecha(self, y):
        if y is None or y.izquierdo is None:
            return y
        x = y.izquierdo
        sub_derecho = x.derecho
        x.derecho = y
        y.izquierdo = sub_derecho
        return x

    def rotar_izquierda(self, x):
        if x is None or x.derecho is None:
            return x
        y = x.derecho
        sub_izquierdo = y.izquierdo
        y.izquierdo = x
        x.derecho = sub_izquierdo
        return y

    def balancear_nodo(self, nodo):
        if nodo is None:
            return None

        balance = self.factor_balance(nodo)
        if balance > 1:
            if self.factor_balance(nodo.izquierdo) < 0:
                nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)
        if balance < -1:
            if self.factor_balance(nodo.derecho) > 0:
                nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)
        return nodo

    def insertar_balanceado(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self.insertar_balanceado(nodo.izquierdo, valor)
        else:
            nodo.derecho = self.insertar_balanceado(nodo.derecho, valor)
        return self.balancear_nodo(nodo)

    def insertar(self, valor):
        self.raiz = self.insertar_balanceado(self.raiz, valor)
        return self.raiz

    def imprimir_inorden(self, nodo=None):
        def _inorden(n):
            if n is None:
                return
            _inorden(n.izquierdo)
            print(n.valor, end=" ")
            _inorden(n.derecho)

        nodo = self.raiz if nodo is None else nodo
        _inorden(nodo)


if __name__ == "__main__":
    arbol = ArbolBinarioOrdenado()
    for valor in [30, 20, 40, 10, 25, 35, 50, 5, 27]:
        arbol.insertar(valor)

    print("Inorden tras inserciones balanceadas:")
    arbol.imprimir_inorden()
    print()
    print("Altura final:", arbol.altura())