class PilaLista:
  def __init__(self, capacidad=None):
    self._datos = []
    self._capacidad = capacidad

  def __len__(self):
    return len(self._datos)

  def esta_vacia(self):
    return len(self._datos) == 0

  def esta_llena(self):
    return self._capacidad is not None and len(self._datos) >= self._capacidad

  def push(self, valor):
    if self.esta_llena():
      raise OverflowError("Pila llena")
    self._datos.append(valor)

  def pop(self):
    if self.esta_vacia():
      raise IndexError("Pila vacia")
    return self._datos.pop()

  def peek(self):
    if self.esta_vacia():
      raise IndexError("Pila vacia")
    return self._datos[-1]

  def imprimir(self):
    print(f"Pila ({len(self)} elementos):")
    for i, valor in enumerate(reversed(self._datos)):
      print(f"  {valor}{' <- top' if i == 0 else ''}")


if __name__ == "__main__":
  pila = PilaLista(capacidad=4)

  for n in (10, 20, 30):
    pila.push(n)
  pila.imprimir()

  print("Peek:", pila.peek())

  while not pila.esta_vacia():
    print("Pop:", pila.pop())