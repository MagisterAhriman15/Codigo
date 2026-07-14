CAPACIDAD = 6


class Cola:
  def __init__(self, capacidad=CAPACIDAD):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.final = 0
    self.cantidad = 0

  def es_vacia(self):
    return self.cantidad == 0

  def es_llena(self):
    return self.final == self.capacidad

  def encolar(self, valor):
    if self.es_llena():
      raise OverflowError("Cola llena")
    self.datos[self.final] = valor
    self.final += 1
    self.cantidad += 1

  def desencolar(self):
    if self.es_vacia():
      raise IndexError("Cola vacia")
    valor = self.datos[self.frente]
    self.frente += 1
    self.cantidad -= 1
    if self.frente == self.final:
      self.frente = 0
      self.final = self.cantidad
    return valor

  def peek(self):
    return None if self.es_vacia() else self.datos[self.frente]

  def imprimir(self):
    contenido = " ".join(str(self.datos[i]) for i in range(self.frente, self.final))
    print(f"[cola] frente={self.frente} final={self.final} cantidad={self.cantidad} -> {contenido}")


if __name__ == "__main__":
  cola = Cola()

  cola.encolar(10)
  cola.encolar(20)
  cola.encolar(30)
  cola.imprimir()

  print("Peek inicial:", cola.peek())

  while not cola.es_vacia():
    valor = cola.desencolar()
    print("Dequeue:", valor)
    if valor == 20:
      cola.encolar(99)

  cola.imprimir()
  print("Estado final vacio:", cola.es_vacia())