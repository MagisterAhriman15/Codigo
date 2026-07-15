CELDA_VACIA = 0
CELDA_OCUPADA = 1
CELDA_BORRADA = 2

class RegistroDNS:
  def __init__(self, dominio, ip):
    self.dominio = dominio
    self.ip = ip


class Entrada:
  def __init__(self, valor=None, estado=CELDA_VACIA):
    self.valor = valor
    self.estado = estado


class TablaDNS:
  def __init__(self, capacidad):
    self.capacidad = capacidad
    self.cantidad = 0
    self.celdas = [Entrada() for _ in range(capacidad)]


def hash1(clave, cap):
  h = 5381
  for caracter in clave:
    h = ((h << 5) + h) + ord(caracter)
  return h % cap


def hash2(clave, cap):
  h = 0
  for caracter in clave:
    h = h * 131 + ord(caracter)
  return 1 + (h % (cap - 1))


def insertar(tabla, dominio, ip):
  base = hash1(dominio, tabla.capacidad)
  paso = hash2(dominio, tabla.capacidad)
  primera_borrada = -1
  for i in range(tabla.capacidad):
    idx = (base + i * paso) % tabla.capacidad
    entrada = tabla.celdas[idx]
    if entrada.estado == CELDA_OCUPADA and entrada.valor.dominio == dominio:
      entrada.valor.ip = ip
      return True
    if entrada.estado == CELDA_BORRADA and primera_borrada == -1:
      primera_borrada = idx
    if entrada.estado == CELDA_VACIA:
      destino = primera_borrada if primera_borrada != -1 else idx
      tabla.celdas[destino] = Entrada(RegistroDNS(dominio, ip), CELDA_OCUPADA)
      tabla.cantidad += 1
      return True
  return False


def buscar(tabla, dominio):
  base = hash1(dominio, tabla.capacidad)
  paso = hash2(dominio, tabla.capacidad)
  for i in range(tabla.capacidad):
    idx = (base + i * paso) % tabla.capacidad
    entrada = tabla.celdas[idx]
    if entrada.estado == CELDA_VACIA:
      return None
    if entrada.estado == CELDA_OCUPADA and entrada.valor.dominio == dominio:
      return entrada.valor
  return None


def eliminar(tabla, dominio):
  base = hash1(dominio, tabla.capacidad)
  paso = hash2(dominio, tabla.capacidad)
  for i in range(tabla.capacidad):
    idx = (base + i * paso) % tabla.capacidad
    entrada = tabla.celdas[idx]
    if entrada.estado == CELDA_VACIA:
      return False
    if entrada.estado == CELDA_OCUPADA and entrada.valor.dominio == dominio:
      entrada.estado = CELDA_BORRADA
      tabla.cantidad -= 1
      return True
  return False


def rehash(tabla, nueva_capacidad):
  nuevas = [Entrada() for _ in range(nueva_capacidad)]
  viejas = tabla.celdas
  tabla.celdas = nuevas
  tabla.capacidad = nueva_capacidad
  tabla.cantidad = 0

  for entrada in viejas:
    if entrada.estado == CELDA_OCUPADA:
      insertar(tabla, entrada.valor.dominio, entrada.valor.ip)
  return True


if __name__ == "__main__":
  tabla = TablaDNS(11)

  dominios = [
    "google.com",
    "facebook.com",
    "wikipedia.org",
    "youtube.com",
    "github.com"
  ]
  ips = [
    "142.250.72.206",
    "157.240.22.35",
    "208.80.154.224",
    "142.250.72.238",
    "140.82.114.4"
  ]
  umbral = 0.7

  for dominio, ip in zip(dominios, ips):
    alpha = (tabla.cantidad + 1) / tabla.capacidad
    if alpha >= umbral:
      nueva = tabla.capacidad * 2 + 1
      print(f"Rehash a {nueva} (alpha previsto {alpha:.2f})")
      rehash(tabla, nueva)
    insertar(tabla, dominio, ip)

  registro = buscar(tabla, "github.com")
  print("github.com ->", registro.ip if registro else "no encontrado")

  insertar(tabla, "google.com", "142.250.72.207")
  registro = buscar(tabla, "google.com")
  print("google.com ->", registro.ip if registro else "no encontrado")

  eliminar(tabla, "facebook.com")
  registro = buscar(tabla, "facebook.com")
  print("facebook.com ->", registro.ip if registro else "no encontrado")