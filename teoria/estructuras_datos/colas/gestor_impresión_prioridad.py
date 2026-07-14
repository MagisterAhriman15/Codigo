CAP_IMP = 20
MAX_NOMBRE_DOC = 48


class Trabajo:
  def __init__(self, archivo="", paginas=0):
    self.archivo = archivo[:MAX_NOMBRE_DOC]
    self.paginas = paginas


class ColaTrabajos:
  def __init__(self, capacidad=CAP_IMP):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.final = 0
    self.cantidad = 0

  def encolar(self, trabajo):
    if self.cantidad == self.capacidad:
      return False
    self.datos[self.final] = trabajo
    self.final = (self.final + 1) % self.capacidad
    self.cantidad += 1
    return True

  def desencolar(self):
    if self.cantidad == 0:
      return None
    trabajo = self.datos[self.frente]
    self.frente = (self.frente + 1) % self.capacidad
    self.cantidad -= 1
    return trabajo


class GestorImpresion:
  def __init__(self):
    self.urgente = ColaTrabajos()
    self.normal = ColaTrabajos()

  def agregar_trabajo(self, archivo, paginas, es_urgente=False):
    trabajo = Trabajo(archivo, paginas)
    return self.urgente.encolar(trabajo) if es_urgente else self.normal.encolar(trabajo)

  def procesar_trabajo(self):
    trabajo = self.urgente.desencolar()
    if trabajo:
      return trabajo
    return self.normal.desencolar()

  def mostrar_estado(self):
    print(f"Urgentes ({self.urgente.cantidad}):")
    idx = self.urgente.frente
    for _ in range(self.urgente.cantidad):
      t = self.urgente.datos[idx]
      print(f"  ! {t.archivo} ({t.paginas} pags)")
      idx = (idx + 1) % self.urgente.capacidad
    print(f"Normales ({self.normal.cantidad}):")
    idx = self.normal.frente
    for _ in range(self.normal.cantidad):
      t = self.normal.datos[idx]
      print(f"  - {t.archivo} ({t.paginas} pags)")
      idx = (idx + 1) % self.normal.capacidad


def main():
  gestor = GestorImpresion()

  while True:
    print("\n1) Agregar trabajo normal")
    print("2) Agregar trabajo urgente")
    print("3) Procesar siguiente")
    print("4) Mostrar estado")
    print("0) Salir")
    opcion = input("Opcion: ").strip()

    if opcion in ("1", "2"):
      archivo = input("Archivo: ").strip()
      try:
        paginas = int(input("Paginas: ").strip())
      except ValueError:
        print("Valor incorrecto")
        continue
      if gestor.agregar_trabajo(archivo, paginas, es_urgente=opcion == "2"):
        print("Trabajo encolado correctamente.")
      else:
        print("Cola correspondiente llena.")
    elif opcion == "3":
      trabajo = gestor.procesar_trabajo()
      if trabajo:
        print(f"Imprimiendo: {trabajo.archivo} ({trabajo.paginas} pags)")
      else:
        print("No hay trabajos pendientes.")
    elif opcion == "4":
      gestor.mostrar_estado()
    elif opcion == "0":
      print("Fin del gestor")
      break
    else:
      print("Opcion no valida")


if __name__ == "__main__":
  main()
  