CAP_VISITANTES = 40
MAX_NOMBRE = 40


class Visitante:
  def __init__(self, nombre=""):
    self.nombre = nombre[:MAX_NOMBRE]


class ColaVisitantes:
  def __init__(self, capacidad=CAP_VISITANTES):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.final = 0
    self.cantidad = 0

  def push(self, visitante):
    if self.cantidad == self.capacidad:
      return False
    self.datos[self.final] = visitante
    self.final = (self.final + 1) % self.capacidad
    self.cantidad += 1
    return True

  def pop(self):
    if self.cantidad == 0:
      return None
    v = self.datos[self.frente]
    self.frente = (self.frente + 1) % self.capacidad
    self.cantidad -= 1
    return v


class ControlAtraccion:
  def __init__(self):
    self.fastpass = ColaVisitantes()
    self.general = ColaVisitantes()
    self.turno_fast = 0
    self.atendidos_fast = 0
    self.atendidos_general = 0

  def registrar(self, nombre, es_fastpass=False):
    visitante = Visitante(nombre)
    return self.fastpass.push(visitante) if es_fastpass else self.general.push(visitante)

  def despachar(self):
    if self.fastpass.cantidad > 0 and (self.turno_fast < 2 or self.general.cantidad == 0):
      v = self.fastpass.pop()
      if v:
        self.turno_fast += 1
        self.atendidos_fast += 1
        return v
    v = self.general.pop()
    if v:
      self.turno_fast = 0
      self.atendidos_general += 1
      return v
    v = self.fastpass.pop()
    if v:
      self.turno_fast = 1
      self.atendidos_fast += 1
      return v
    return None

  def mostrar(self):
    print(f"FastPass ({self.fastpass.cantidad}):")
    idx = self.fastpass.frente
    for _ in range(self.fastpass.cantidad):
      v = self.fastpass.datos[idx]
      print(f"  FP - {v.nombre}")
      idx = (idx + 1) % self.fastpass.capacidad
    print(f"General ({self.general.cantidad}):")
    idx = self.general.frente
    for _ in range(self.general.cantidad):
      v = self.general.datos[idx]
      print(f"  GEN - {v.nombre}")
      idx = (idx + 1) % self.general.capacidad

  def reporte(self):
    print("--- Resumen ---")
    print(f"Atendidos FastPass: {self.atendidos_fast}")
    print(f"Atendidos General: {self.atendidos_general}")


def main():
  control = ControlAtraccion()

  while True:
    print("\n1) Registrar visitante general")
    print("2) Registrar visitante FastPass")
    print("3) Despachar siguiente")
    print("4) Mostrar colas")
    print("0) Cerrar atraccion")
    opcion = input("Opcion: ").strip()

    if opcion in ("1", "2"):
      nombre = input("Nombre: ").strip()
      if control.registrar(nombre, es_fastpass=opcion == "2"):
        print("Registrado.")
      else:
        print("Cola completa.")
    elif opcion == "3":
      visitante = control.despachar()
      if visitante:
        print(f"Ingresando: {visitante.nombre}")
      else:
        print("No hay visitantes en espera.")
    elif opcion == "4":
      control.mostrar()
      control.reporte()
    elif opcion == "0":
      print("Atraccion cerrada.")
      control.reporte()
      break
    else:
      print("Opcion no valida.")


if __name__ == "__main__":
  main()