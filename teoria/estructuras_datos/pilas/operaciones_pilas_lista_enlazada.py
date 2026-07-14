class Nodo:
  def __init__(self, valor, sig=None):
    self.valor = valor
    self.sig = sig


class PilaEnlazada:
  def __init__(self):
    self.tope = None
    self._largo = 0

  def __len__(self):
    return self._largo

  def esta_vacia(self):
    return self.tope is None

  def push(self, valor):
    self.tope = Nodo(valor, self.tope)
    self._largo += 1

  def pop(self):
    if self.esta_vacia():
      raise IndexError("Pila vacia")
    valor = self.tope.valor
    self.tope = self.tope.sig
    self._largo -= 1
    return valor

  def peek(self):
    if self.esta_vacia():
      raise IndexError("Pila vacia")
    return self.tope.valor

  def limpiar(self):
    self.tope = None
    self._largo = 0

  def imprimir(self):
    print(f"Pila enlazada ({len(self)} nodos):")
    actual = self.tope
    while actual:
      sufijo = " <- top" if actual is self.tope else ""
      print(f"  {actual.valor}{sufijo}")
      actual = actual.sig


if __name__ == "__main__":
  pila = PilaEnlazada()

  for n in (2, 4, 6, 8):
    pila.push(n)
  pila.imprimir()

  print("Peek:", pila.peek())

  while not pila.esta_vacia():
    print("Pop:", pila.pop())