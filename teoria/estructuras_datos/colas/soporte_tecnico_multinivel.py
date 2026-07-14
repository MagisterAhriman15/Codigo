CAP_TICKETS = 40
MAX_CLIENTE = 40
MAX_NOTA = 64


class Ticket:
  def __init__(self, cliente="", nota="", nivel=1):
    self.cliente = cliente[:MAX_CLIENTE]
    self.nota = nota[:MAX_NOTA]
    self.nivel = nivel


class ColaTickets:
  def __init__(self, capacidad=CAP_TICKETS):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.final = 0
    self.cantidad = 0

  def encolar(self, ticket):
    if self.cantidad == self.capacidad:
      return False
    self.datos[self.final] = ticket
    self.final = (self.final + 1) % self.capacidad
    self.cantidad += 1
    return True

  def desencolar(self):
    if self.cantidad == 0:
      return None
    ticket = self.datos[self.frente]
    self.frente = (self.frente + 1) % self.capacidad
    self.cantidad -= 1
    return ticket


class CentroSoporte:
  def __init__(self):
    self.basic = ColaTickets()
    self.mid = ColaTickets()
    self.expert = ColaTickets()
    self.atendidos = [0, 0, 0]  # basico, intermedio, experto

  def registrar_ticket(self, cliente, nota, nivel):
    cola = self.expert if nivel == 3 else (self.mid if nivel == 2 else self.basic)
    ticket = Ticket(cliente, nota, nivel)
    return cola.encolar(ticket)

  def atender_ticket(self):
    for idx, cola in enumerate([self.expert, self.mid, self.basic]):
      ticket = cola.desencolar()
      if ticket:
        self.atendidos[2 - idx] += 1
        return ticket
    return None

  def escalar_ticket(self, origen, destino):
    if origen < 1 or origen > 3 or destino < 1 or destino > 3 or destino <= origen:
      return False
    colas = [self.basic, self.mid, self.expert]
    if colas[origen - 1].cantidad == 0:
      return False
    ticket = colas[origen - 1].desencolar()
    ticket.nivel = destino
    return colas[destino - 1].encolar(ticket)

  def mostrar_estado(self):
    print(f"Experto: {self.expert.cantidad} pendientes")
    print(f"Intermedio: {self.mid.cantidad} pendientes")
    print(f"Basico: {self.basic.cantidad} pendientes")


def leer_entero(mensaje):
  valor = input(mensaje).strip()
  try:
    return int(valor)
  except ValueError:
    print("Entrada invalida")
    return None


def main():
  centro = CentroSoporte()

  while True:
    print("\n1) Registrar ticket basico")
    print("2) Registrar ticket intermedio")
    print("3) Registrar ticket experto")
    print("4) Atender siguiente ticket")
    print("5) Escalar ticket")
    print("6) Mostrar estado")
    print("0) Cerrar turno")
    opcion = input("Opcion: ").strip()

    if opcion in ("1", "2", "3"):
      cliente = input("Cliente: ").strip()
      nota = input("Resumen: ").strip()
      nivel = int(opcion)
      if centro.registrar_ticket(cliente, nota, nivel):
        print("Ticket registrado.")
      else:
        print("Cola correspondiente llena.")
    elif opcion == "4":
      ticket = centro.atender_ticket()
      if ticket:
        print(f"Atendiendo [{ticket.nivel}] {ticket.cliente} - {ticket.nota}")
      else:
        print("No hay tickets pendientes.")
    elif opcion == "5":
      origen = leer_entero("Nivel origen (1-3): ")
      destino = leer_entero("Nivel destino (1-3): ")
      if origen is None or destino is None:
        continue
      if centro.escalar_ticket(origen, destino):
        print("Escalamiento realizado.")
      else:
        print("No se pudo escalar (verifica niveles y disponibilidad).")
    elif opcion == "6":
      centro.mostrar_estado()
    elif opcion == "0":
      print("Turno cerrado.")
      centro.mostrar_estado()
      print(f"Atendidos experto: {centro.atendidos[2]}")
      print(f"Atendidos intermedio: {centro.atendidos[1]}")
      print(f"Atendidos basico: {centro.atendidos[0]}")
      break
    else:
      print("Opcion no valida.")


if __name__ == "__main__":
  main()