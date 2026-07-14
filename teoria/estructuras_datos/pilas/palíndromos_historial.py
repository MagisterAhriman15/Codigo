def normalizar(texto):
  limpio = []
  for c in texto:
    if c.isalnum():
      limpio.append(c.lower())
  return "".join(limpio)


def es_palindromo(texto):
  limpio = normalizar(texto)
  return limpio == limpio[::-1]


class Verificador:
  def __init__(self):
    self.historial = []
    self.redo_stack = []

  def check(self, texto):
    resultado = f'"{texto}" => {"PALINDROMO" if es_palindromo(texto) else "NO PALINDROMO"}'
    self.historial.append(resultado)
    self.redo_stack.clear()
    return resultado

  def undo(self):
    if not self.historial:
      return "Nada para deshacer"
    valor = self.historial.pop()
    self.redo_stack.append(valor)
    return self.historial[-1] if self.historial else "Historial vacio"

  def rehacer(self):
    if not self.redo_stack:
      return "Nada para rehacer"
    valor = self.redo_stack.pop()
    self.historial.append(valor)
    return valor


if __name__ == "__main__":
  v = Verificador()
  print(v.check("Anita lava la tina"))
  print(v.check("Hola mundo"))
  print("Undo ->", v.undo())
  print("Redo ->", v.rehacer())
  print(v.check("Yo hago yoga hoy"))
  print("Top:", v.historial[-1])