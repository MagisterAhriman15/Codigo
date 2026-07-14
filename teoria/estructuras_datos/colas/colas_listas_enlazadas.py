class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None


class ColaLista:
  def __init__(self):
    self.frente = None
    self.final = None
    self.cantidad = 0

  def encolar(self, valor):
    nuevo = Nodo(valor)
    if not self.frente:
      self.frente = nuevo
    else:
      self.final.siguiente = nuevo
    self.final = nuevo
    self.cantidad += 1

  def desencolar(self):
    if not self.frente:
      return None
    nodo = self.frente
    self.frente = nodo.siguiente
    if not self.frente:
      self.final = None
    self.cantidad -= 1
    return nodo.dato

  def imprimir(self):
    elementos = []
    actual = self.frente
    while actual:
      elementos.append(str(actual.dato))
      actual = actual.siguiente
    print(f"[cola] cantidad={self.cantidad} -> {' '.join(elementos)}")

  def vaciar(self):
    while self.desencolar() is not None:
      pass


if __name__ == "__main__":
  cola = ColaLista()

  for i in range(1, 4):
    cola.encolar(i * 10)
  cola.imprimir()

  valor = cola.desencolar()
  print("desencolado:", valor)
  cola.imprimir()

  cola.encolar(99)
  cola.encolar(100)
  cola.imprimir()

  while cola.cantidad:
    valor = cola.desencolar()
    print("procesado:", valor)
  cola.imprimir()

  cola.vaciar()