class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.anterior = None
    self.siguiente = None


class Deque:
  def __init__(self):
    self.frente = None
    self.final = None
    self.cantidad = 0

  def push_front(self, valor):
    nuevo = Nodo(valor)
    nuevo.siguiente = self.frente
    if self.frente:
      self.frente.anterior = nuevo
    else:
      self.final = nuevo
    self.frente = nuevo
    self.cantidad += 1

  def push_back(self, valor):
    nuevo = Nodo(valor)
    nuevo.anterior = self.final
    if self.final:
      self.final.siguiente = nuevo
    else:
      self.frente = nuevo
    self.final = nuevo
    self.cantidad += 1

  def pop_front(self):
    if not self.frente:
      return None
    nodo = self.frente
    self.frente = nodo.siguiente
    if self.frente:
      self.frente.anterior = None
    else:
      self.final = None
    self.cantidad -= 1
    return nodo.dato

  def pop_back(self):
    if not self.final:
      return None
    nodo = self.final
    self.final = nodo.anterior
    if self.final:
      self.final.siguiente = None
    else:
      self.frente = None
    self.cantidad -= 1
    return nodo.dato

  def imprimir(self):
    elementos = []
    actual = self.frente
    while actual:
      elementos.append(str(actual.dato))
      actual = actual.siguiente
    print(f"[deque] cantidad={self.cantidad} -> {' '.join(elementos)}")


if __name__ == "__main__":
  deque = Deque()

  deque.push_back(10)
  deque.push_back(20)
  deque.push_front(5)
  deque.imprimir()

  print("pop_front =", deque.pop_front())
  deque.imprimir()

  deque.push_front(1)
  deque.push_back(99)
  deque.imprimir()

  print("pop_back =", deque.pop_back())
  deque.imprimir()