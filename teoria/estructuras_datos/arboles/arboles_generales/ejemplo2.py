class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.hijos = []

  def agregar_hijo(self, nodo_hijo):
    if nodo_hijo is None:
      return
    self.hijos.append(nodo_hijo)


class ArbolGeneral:
  def __init__(self):
    self.raiz = None

  def crear_raiz(self, valor):
    if self.raiz is None:
      self.raiz = Nodo(valor)
    return self.raiz

  def agregar_hijo(self, padre, valor):
    nuevo = Nodo(valor)
    padre.agregar_hijo(nuevo)
    return nuevo

  def imprimir(self, nodo=None, sangria=0):
    nodo = nodo or self.raiz
    if nodo is None:
      return
    print("  " * sangria + f"-{nodo.valor}")
    for hijo in nodo.hijos:
      self.imprimir(hijo, sangria + 1)

  def crear_arbol_demo(self):
    self.raiz = Nodo(1)
    nodo_a = Nodo(2)
    nodo_b = Nodo(3)
    nodo_c = Nodo(4)
    self.raiz.agregar_hijo(nodo_c)
    self.raiz.agregar_hijo(nodo_b)
    self.raiz.agregar_hijo(nodo_a)

    nodo_d = Nodo(5)
    nodo_e = Nodo(6)
    nodo_b.agregar_hijo(nodo_e)
    nodo_b.agregar_hijo(nodo_d)
    return self.raiz


if __name__ == "__main__":
  arbol = ArbolGeneral()
  arbol.crear_arbol_demo()
  print("Arbol con lista dinamica de hijos:")
  arbol.imprimir()