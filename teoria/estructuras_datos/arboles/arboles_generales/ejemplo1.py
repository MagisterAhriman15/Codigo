class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.primer_hijo = None
    self.siguiente_hermano = None
    self.padre = None


class ArbolGeneral:
  def __init__(self):
    self.raiz = None
    self.cantidad = 0

  def enlazar_como_primer_hijo(self, padre, nuevo_hijo):
    if padre is None or nuevo_hijo is None:
      return
    nuevo_hijo.padre = padre
    nuevo_hijo.siguiente_hermano = padre.primer_hijo
    padre.primer_hijo = nuevo_hijo

  def enlazar_como_hermano(self, referencia, nuevo_hermano):
    if referencia is None or nuevo_hermano is None:
      return
    nuevo_hermano.padre = referencia.padre
    nuevo_hermano.siguiente_hermano = referencia.siguiente_hermano
    referencia.siguiente_hermano = nuevo_hermano

  def contar_subarbol(self, nodo):
    if nodo is None:
      return 0
    total = 1
    hijo = nodo.primer_hijo
    while hijo:
      total += self.contar_subarbol(hijo)
      hijo = hijo.siguiente_hermano
    return total

  def grado_nodo(self, nodo):
    grado = 0
    hijo = nodo.primer_hijo if nodo else None
    while hijo:
      grado += 1
      hijo = hijo.siguiente_hermano
    return grado

  def profundidad(self, nodo):
    nivel = 0
    while nodo and nodo.padre:
      nodo = nodo.padre
      nivel += 1
    return nivel

  def altura(self, nodo):
    if nodo is None:
      return 0
    max_hijos = 0
    hijo = nodo.primer_hijo
    while hijo:
      max_hijos = max(max_hijos, self.altura(hijo))
      hijo = hijo.siguiente_hermano
    return 1 + max_hijos

  def imprimir_arbol(self, nodo=None, sangria=0):
    nodo = nodo or self.raiz
    if nodo is None:
      return
    print("  " * sangria + f"-{nodo.valor}")
    hijo = nodo.primer_hijo
    while hijo:
      self.imprimir_arbol(hijo, sangria + 1)
      hijo = hijo.siguiente_hermano

  def crear_arbol_demo(self):
    self.raiz = Nodo(1)
    self.cantidad = 1

    nodo_a = Nodo(2)
    nodo_b = Nodo(3)
    nodo_c = Nodo(4)
    self.enlazar_como_primer_hijo(self.raiz, nodo_b)
    self.enlazar_como_primer_hijo(self.raiz, nodo_a)
    self.enlazar_como_hermano(nodo_a, nodo_c)
    self.cantidad += 3

    nodo_d = Nodo(5)
    nodo_e = Nodo(6)
    self.enlazar_como_primer_hijo(nodo_b, nodo_d)
    self.enlazar_como_hermano(nodo_d, nodo_e)
    self.cantidad += 2
    return nodo_e


if __name__ == "__main__":
  arbol = ArbolGeneral()
  nodo_e = arbol.crear_arbol_demo()
  print("Representacion del arbol:")
  arbol.imprimir_arbol()
  print(f"Cantidad total de nodos: {arbol.contar_subarbol(arbol.raiz)}")
  print(f"Grado de la raiz: {arbol.grado_nodo(arbol.raiz)}")
  print(f"Altura del arbol: {arbol.altura(arbol.raiz)}")
  print(f"Profundidad de nodo_e: {arbol.profundidad(nodo_e)}")