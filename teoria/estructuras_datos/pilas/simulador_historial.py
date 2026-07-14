class Historial:
  def __init__(self, home: str):
    self.back = [home]
    self.forward = []
    self.actual = home

  def visitar(self, url: str):
    self.back.append(url)
    self.forward.clear()
    self.actual = url

  def atras(self):
    if len(self.back) <= 1:
      return self.actual
    previo = self.back.pop()
    self.forward.append(previo)
    self.actual = self.back[-1]
    return self.actual

  def adelante(self):
    if not self.forward:
      return self.actual
    siguiente = self.forward.pop()
    self.back.append(siguiente)
    self.actual = siguiente
    return self.actual

  def imprimir(self):
    print(f"Pagina actual: {self.actual}")
    print("BACK:")
    for url in reversed(self.back):
      sufijo = " <- top" if url == self.back[-1] else ""
      print(f"  {url}{sufijo}")
    print("FORWARD:")
    for url in reversed(self.forward):
      sufijo = " <- top" if url == (self.forward[-1] if self.forward else None) else ""
      print(f"  {url}{sufijo}")


if __name__ == "__main__":
  hist = Historial("https://inicio.com")
  hist.visitar("https://noticias.com")
  hist.visitar("https://docs.com")
  hist.atras()
  hist.adelante()
  hist.visitar("https://foros.com")
  hist.imprimir()