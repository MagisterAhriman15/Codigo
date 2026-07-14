CAPACIDAD = 8


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
    if self.frente == self.final:  # reinicio simple para reutilizar espacio
      self.frente = 0
      self.final = self.cantidad
    return valor

  def imprimir(self):
    contenido = " ".join(str(self.datos[i]) for i in range(self.frente, self.final))
    print(f"[cola] frente={self.frente} final={self.final} cantidad={self.cantidad} -> {contenido}")


if __name__ == "__main__":
  cola = Cola()

  for i in range(1, 6):
    cola.encolar(i * 10)
  cola.imprimir()

  while not cola.es_vacia():
    valor = cola.desencolar()
    print("Desencolado:", valor)
    if valor == 20:
      cola.encolar(99)
  cola.imprimir()