CAP_RESERVAS = 30
MAX_NOMBRE = 48


class Reserva:
  def __init__(self, nombre="", comensales=0):
    self.nombre = nombre[:MAX_NOMBRE]
    self.comensales = comensales


class ColaReservas:
  def __init__(self, capacidad=CAP_RESERVAS):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.final = 0
    self.cantidad = 0

  def encolar(self, reserva):
    if self.cantidad == self.capacidad:
      return False
    self.datos[self.final] = reserva
    self.final = (self.final + 1) % self.capacidad
    self.cantidad += 1
    return True

  def desencolar(self):
    if self.cantidad == 0:
      return None
    res = self.datos[self.frente]
    self.frente = (self.frente + 1) % self.capacidad
    self.cantidad -= 1
    return res


class Restaurante:
  def __init__(self, cupo_terraza):
    self.salon = ColaReservas()
    self.terraza = ColaReservas()
    self.atendidos_salon = 0
    self.atendidos_terraza = 0
    self.cupo_terraza = cupo_terraza

  def registrar_reserva(self, nombre, comensales, en_terraza=False):
    reserva = Reserva(nombre, comensales)
    return self.terraza.encolar(reserva) if en_terraza else self.salon.encolar(reserva)

  def asignar_mesa(self):
    if self.terraza.cantidad > 0:
      siguiente = self.terraza.datos[self.terraza.frente]
      if self.atendidos_terraza + siguiente.comensales <= self.cupo_terraza:
        reserva = self.terraza.desencolar()
        self.atendidos_terraza += reserva.comensales
        return reserva, "Terraza"
    reserva = self.salon.desencolar()
    if reserva:
      self.atendidos_salon += reserva.comensales
      return reserva, "Salon"
    reserva = self.terraza.desencolar()
    if reserva:
      self.atendidos_terraza += reserva.comensales
      return reserva, "Terraza"
    return None, None

  def mostrar_estado(self):
    print(f"Terraza: {self.terraza.cantidad} reservas en espera, {self.atendidos_terraza} comensales acomodados")
    print(f"Salon: {self.salon.cantidad} reservas en espera, {self.atendidos_salon} comensales acomodados")


def leer_entero(mensaje):
  valor = input(mensaje).strip()
  try:
    return int(valor)
  except ValueError:
    print("Valor invalido")
    return None


def main():
  restaurante = Restaurante(cupo_terraza=80)

  while True:
    print("\n1) Registrar reserva salon")
    print("2) Registrar reserva terraza")
    print("3) Asignar mesa")
    print("4) Mostrar estado")
    print("0) Cerrar turno")
    opcion = input("Opcion: ").strip()

    if opcion in ("1", "2"):
      nombre = input("Nombre: ").strip()
      comensales = leer_entero("Comensales: ")
      if comensales is None:
        continue
      if restaurante.registrar_reserva(nombre, comensales, en_terraza=opcion == "2"):
        print("Reserva registrada.")
      else:
        print("Cola llena.")
    elif opcion == "3":
      reserva, ambiente = restaurante.asignar_mesa()
      if reserva:
        print(f"Asignado a {reserva.nombre} ({reserva.comensales} personas) -> {ambiente}")
      else:
        print("No hay reservas pendientes.")
    elif opcion == "4":
      restaurante.mostrar_estado()
    elif opcion == "0":
      print("Turno cerrado.")
      restaurante.mostrar_estado()
      break
    else:
      print("Opcion no valida.")


if __name__ == "__main__":
  main()