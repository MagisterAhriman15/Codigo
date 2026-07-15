class Nodo:
    def __init__(self, valor=None, operador=None, es_operador=False):
        self.valor = valor
        self.operador = operador
        self.es_operador = es_operador
        self.izquierdo = None
        self.derecho = None


class ArbolExpresion:
    def crear_operando(self, valor):
        return Nodo(valor=valor, es_operador=False)

    def crear_operador(self, operador, izquierdo, derecho):
        nodo = Nodo(operador=operador, es_operador=True)
        nodo.izquierdo = izquierdo
        nodo.derecho = derecho
        return nodo

    def evaluar(self, nodo):
        if nodo is None:
            return 0
        if not nodo.es_operador:
            return nodo.valor
        izq = self.evaluar(nodo.izquierdo)
        der = self.evaluar(nodo.derecho)
        return izq + der if nodo.operador == "+" else izq - der

    def imprimir_infijo(self, nodo):
        if nodo is None:
            return
        if nodo.es_operador:
            print("(", end="")
        self.imprimir_infijo(nodo.izquierdo)
        if nodo.es_operador:
            print(f" {nodo.operador} ", end="")
        else:
            print(nodo.valor, end="")
        self.imprimir_infijo(nodo.derecho)
        if nodo.es_operador:
            print(")", end="")


if __name__ == "__main__":
    arbol = ArbolExpresion()
    n12 = arbol.crear_operando(12)
    n8 = arbol.crear_operando(8)
    n3 = arbol.crear_operando(3)
    n5 = arbol.crear_operando(5)
    n4 = arbol.crear_operando(4)

    sub = arbol.crear_operador("-", n8, n3)       # (8 - 3)
    sum12 = arbol.crear_operador("+", n12, sub)   # 12 + (8 - 3)
    sum5 = arbol.crear_operador("+", n5, n4)      # (5 + 4)
    raiz = arbol.crear_operador("-", sum12, sum5) # (12 + (8 - 3)) - (5 + 4)

    print("Expresion infija:", end=" ")
    arbol.imprimir_infijo(raiz)
    print()
    print("Resultado:", arbol.evaluar(raiz))