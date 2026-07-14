class Editor:
  def __init__(self):
    self.lineas = []
    self.undo = []
    self.redo = []

  def add(self, texto):
    self.lineas.append(texto)
    self.undo.append(("ADD", texto))
    self.redo.clear()

  def delete(self):
    if not self.lineas:
      return "Nada para borrar"
    texto = self.lineas.pop()
    self.undo.append(("DEL", texto))
    self.redo.clear()
    return texto

  def mostrar(self):
    print("----- Documento -----")
    for i, linea in enumerate(self.lineas, 1):
      print(f"{i}: {linea}")

  def do_undo(self):
    if not self.undo:
      return "Nada que deshacer"
    op, texto = self.undo.pop()
    if op == "ADD":
      borrado = self.lineas.pop() if self.lineas else None
      self.redo.append(("ADD", texto))
      return f"Deshecho ADD: {borrado}"
    if op == "DEL":
      self.lineas.append(texto)
      self.redo.append(("DEL", texto))
      return f"Deshecho DEL: {texto}"

  def do_redo(self):
    if not self.redo:
      return "Nada que rehacer"
    op, texto = self.redo.pop()
    if op == "ADD":
      self.lineas.append(texto)
    elif op == "DEL" and self.lineas:
      self.lineas.pop()
    self.undo.append((op, texto))
    return f"Rehecho {op}: {texto}"


if __name__ == "__main__":
  ed = Editor()
  ed.add("Linea 1")
  ed.add("Linea 2")
  ed.mostrar()
  print(ed.delete())
  print(ed.do_undo())
  print(ed.do_redo())
  ed.add("Linea 3")
  ed.mostrar()