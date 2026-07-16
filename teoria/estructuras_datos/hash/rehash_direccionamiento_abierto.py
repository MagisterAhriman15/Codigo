CELDA_VACIA = 0
CELDA_OCUPADA = 1
CELDA_BORRADA = 2

class Entrada:
  def __init__(self, clave=None, valor=0, estado=CELDA_VACIA):
    self.clave = clave
    self.valor = valor
    self.estado = estado


class HashOA:
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


def insertar_sin_rehash(tabla, clave, valor):
  base = hash1(clave, tabla.capacidad)
  paso = hash2(clave, tabla.capacidad)
  primera_borrada = -1
  for i in range(tabla.capacidad):
    idx = (base + i * paso) % tabla.capacidad
    entrada = tabla.celdas[idx]
    if entrada.estado == CELDA_OCUPADA and entrada.clave == clave:
      entrada.valor = valor
      return True
    if entrada.estado == CELDA_BORRADA and primera_borrada == -1:
      primera_borrada = idx
    if entrada.estado == CELDA_VACIA:
      destino = primera_borrada if primera_borrada != -1 else idx
      tabla.celdas[destino] = Entrada(clave, valor, CELDA_OCUPADA)
      tabla.cantidad += 1
      return True
  return False


def hash_oa_rehash(tabla, nueva_capacidad):
  nuevas = [Entrada() for _ in range(nueva_capacidad)]
  viejas = tabla.celdas
  tabla.celdas = nuevas
  tabla.capacidad = nueva_capacidad
  tabla.cantidad = 0

  for entrada in viejas:
    if entrada.estado == CELDA_OCUPADA:
      insertar_sin_rehash(tabla, entrada.clave, entrada.valor)
  return True


def imprimir(tabla):
  for i in range(tabla.capacidad):
    entrada = tabla.celdas[i]
    if entrada.estado == CELDA_OCUPADA:
      print(f"[{i}] ({entrada.clave} -> {entrada.valor})")
    elif entrada.estado == CELDA_BORRADA:
      print(f"[{i}] ")
    else:
      print(f"[{i}] ")


if __name__ == "__main__":
  tabla = HashOA(7)
  claves = ["juan", "ana", "luis", "pedro", "maria", "sofia"]
  valores = [50, 23, 19, 90, 41, 77]
  umbral = 0.7

  for i in range(len(claves)):
    alpha = (tabla.cantidad + 1) / tabla.capacidad
    if alpha >= umbral:
      nueva = tabla.capacidad * 2 + 1
      print(f"Rehash a capacidad {nueva} (alpha previsto {alpha:.2f})")
      hash_oa_rehash(tabla, nueva)
    insertar_sin_rehash(tabla, claves[i], valores[i])

  print("Tabla final:")
  imprimir(tabla)

  hash_oa_rehash(tabla, tabla.capacidad * 2 + 1)
  print("Tras rehash manual:")
  imprimir(tabla)