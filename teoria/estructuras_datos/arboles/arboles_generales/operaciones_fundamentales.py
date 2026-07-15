class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.primer_hijo = None
    self.siguiente_hermano = None
    self.padre = None


class ArbolGeneral:
  def __init__(self):
    self.raiz = None

  def crear_raiz(self, valor):
    if self.raiz is None:
      self.raiz = Nodo(valor)
    return self.raiz

  def agregar_hijo(self, padre, valor):
    if padre is None:
      return None
    nuevo = Nodo(valor)
    nuevo.padre = padre
    if padre.primer_hijo is None:
      padre.primer_hijo = nuevo
      return nuevo
    actual = padre.primer_hijo
    while actual.siguiente_hermano:
      actual = actual.siguiente_hermano
    actual.siguiente_hermano = nuevo
    return nuevo

  def contar_nodos(self, nodo):
    if nodo is None:
      return 0
    total = 1
    hijo = nodo.primer_hijo
    while hijo:
      total += self.contar_nodos(hijo)
      hijo = hijo.siguiente_hermano
    return total

  def contar_hojas(self, nodo):
    if nodo is None:
      return 0
    if nodo.primer_hijo is None:
      return 1
    hojas = 0
    hijo = nodo.primer_hijo
    while hijo:
      hojas += self.contar_hojas(hijo)
      hijo = hijo.siguiente_hermano
    return hojas

  def contar_hijos(self, nodo):
    grado = 0
    hijo = nodo.primer_hijo if nodo else None
    while hijo:
      grado += 1
      hijo = hijo.siguiente_hermano
    return grado

  def altura(self, nodo):
    if nodo is None:
      return 0
    max_altura = 0
    hijo = nodo.primer_hijo
    while hijo:
      altura_hijo = self.altura(hijo)
      if altura_hijo > max_altura:
        max_altura = altura_hijo
      hijo = hijo.siguiente_hermano
    return 1 + max_altura

  def buscar_valor(self, nodo, objetivo):
    if nodo is None:
      return None
    if nodo.valor == objetivo:
      return nodo
    hijo = nodo.primer_hijo
    while hijo:
      resultado = self.buscar_valor(hijo, objetivo)
      if resultado:
        return resultado
      hijo = hijo.siguiente_hermano
    return None

  def calcular_profundidades(self, nodo, profundidad, fn, ctx=None):
    if nodo is None or fn is None:
      return
    fn(nodo, profundidad, ctx)
    hijo = nodo.primer_hijo
    while hijo:
      self.calcular_profundidades(hijo, profundidad + 1, fn, ctx)
      hijo = hijo.siguiente_hermano

  def obtener_hijos(self, nodo):
    hijos = []
    hijo = nodo.primer_hijo if nodo else None
    while hijo:
      hijos.append(hijo)
      hijo = hijo.siguiente_hermano
    return hijos

  def son_iguales(self, a, b):
    if a is None and b is None:
      return True
    if a is None or b is None or a.valor != b.valor:
      return False
    hijo_a = a.primer_hijo
    hijo_b = b.primer_hijo
    while hijo_a and hijo_b:
      if not self.son_iguales(hijo_a, hijo_b):
        return False
      hijo_a = hijo_a.siguiente_hermano
      hijo_b = hijo_b.siguiente_hermano
    return hijo_a is None and hijo_b is None

  def crear_demo(self):
    raiz = self.crear_raiz("A")
    b = self.agregar_hijo(raiz, "B")
    c = self.agregar_hijo(raiz, "C")
    self.agregar_hijo(raiz, "D")
    self.agregar_hijo(b, "B1")
    self.agregar_hijo(b, "B2")
    self.agregar_hijo(c, "C1")
    return raiz


def mostrar_profundidad(nodo, profundidad, _):
  print(f"{nodo.valor}: {profundidad}")


if __name__ == "__main__":
  arbol = ArbolGeneral()
  raiz = arbol.crear_demo()
  print(f"Total de nodos: {arbol.contar_nodos(raiz)}")
  print(f"Total de hojas: {arbol.contar_hojas(raiz)}")
  print(f"Altura: {arbol.altura(raiz)}")
  print(f"Hijos de A: {arbol.contar_hijos(raiz)}")
  encontrado = arbol.buscar_valor(raiz, "C1")
  print(f"Buscar C1: {encontrado.valor if encontrado else 'No encontrado'}")
  print("Profundidades:")
  arbol.calcular_profundidades(raiz, 0, mostrar_profundidad)
  print(f"Lista de hijos de B: {[nodo.valor for nodo in arbol.obtener_hijos(arbol.buscar_valor(raiz, 'B'))]}")