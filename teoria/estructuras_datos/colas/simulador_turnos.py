CAP_TURNOS = 16
MAX_NOMBRE = 32


class Cliente:
  def __init__(self, ticket=0, nombre=""):
    self.ticket = ticket
    self.nombre = nombre


class ColaTurnos:
  def __init__(self, capacidad=CAP_TURNOS):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.final = 0
    self.cantidad = 0
    self.siguiente_ticket = 1

  def agregar_cliente(self, nombre):
    if self.cantidad == self.capacidad:
      return 0
    slot = Cliente(self.siguiente_ticket, nombre[:MAX_NOMBRE])
    self.datos[self.final] = slot
    self.siguiente_ticket += 1
    self.final = (self.final + 1) % self.capacidad
    self.cantidad += 1
    return slot.ticket

  def llamar_cliente(self):
    if self.cantidad == 0:
      return None
    cliente = self.datos[self.frente]
    self.frente = (self.frente + 1) % self.capacidad
    self.cantidad -= 1
    return cliente

  def mostrar_cola(self):
    print(f"Turnos pendientes ({self.cantidad}):")
    idx = self.frente
    for _ in range(self.cantidad):
      slot = self.datos[idx]
      print(f"  #{slot.ticket} - {slot.nombre}")
      idx = (idx + 1) % self.capacidad


def main():
  cola = ColaTurnos()

  while True:
    print("1) Agregar cliente")
    print("2) Llamar siguiente")
    print("3) Mostrar cola")
    print("0) Salir")
    opcion = input("Opcion: ").strip()

    if opcion == "1":
      nombre = input("Nombre: ").strip()
      ticket = cola.agregar_cliente(nombre)
      if ticket == 0:
        print("Cola llena, intenta mas tarde.")
      else:
        print(f"Ticket asignado: #{ticket}")
    elif opcion == "2":
      cliente = cola.llamar_cliente()
      if cliente:
        print(f"Atendiendo #{cliente.ticket} - {cliente.nombre}")
      else:
        print("No hay clientes esperando.")
    elif opcion == "3":
      cola.mostrar_cola()
    elif opcion == "0":
      print("Hasta luego")
      break
    else:
      print("Opcion no valida")


if __name__ == "__main__":
  main()