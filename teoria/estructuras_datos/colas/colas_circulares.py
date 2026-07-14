CAP_CIRC = 5


def siguiente(idx, capacidad):
  return (idx + 1) % capacidad


class ColaCircular:
  def __init__(self, capacidad=CAP_CIRC):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.final = 0
    self.cantidad = 0

  def encolar(self, valor):
    if self.cantidad == self.capacidad:
      raise OverflowError("Cola llena")
    self.datos[self.final] = valor
    self.final = siguiente(self.final, self.capacidad)
    self.cantidad += 1

  def desencolar(self):
    if self.cantidad == 0:
      raise IndexError("Cola vacia")
    valor = self.datos[self.frente]
    self.frente = siguiente(self.frente, self.capacidad)
    self.cantidad -= 1
    return valor

  def imprimir(self):
    recorrido = []
    idx = self.frente
    for _ in range(self.cantidad):
      recorrido.append(str(self.datos[idx]))
      idx = siguiente(idx, self.capacidad)
    print(f"[circular] frente={self.frente} final={self.final} cantidad={self.cantidad} -> {' '.join(recorrido)}")


if __name__ == "__main__":
  cola = ColaCircular()

  for i in range(4):
    cola.encolar(i + 1)
  cola.imprimir()

  cola.desencolar()
  cola.desencolar()
  cola.imprimir()

  cola.encolar(99)
  cola.encolar(100)
  cola.imprimir()

  while cola.cantidad:
    valor = cola.desencolar()
    print("consumido:", valor)
  cola.imprimir()