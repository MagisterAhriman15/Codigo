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


def hash_buscar(tabla, clave):
  base = hash1(clave, tabla.capacidad)
  paso = hash2(clave, tabla.capacidad)
  for i in range(tabla.capacidad):
    idx = (base + i * paso) % tabla.capacidad
    entrada = tabla.celdas[idx]
    if entrada.estado == CELDA_VACIA:
      return None
    if entrada.estado == CELDA_OCUPADA and entrada.clave == clave:
      return entrada
  return None


def hash_insertar(tabla, clave, valor):
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


def hash_eliminar(tabla, clave):
  entrada = hash_buscar(tabla, clave)
  if not entrada:
    return False
  entrada.estado = CELDA_BORRADA
  tabla.cantidad -= 1
  return True


def hash_imprimir(tabla):
  for i in range(tabla.capacidad):
    entrada = tabla.celdas[i]
    if entrada.estado == CELDA_OCUPADA:
      print(f"[{i}] ({entrada.clave} -> {entrada.valor})")
    elif entrada.estado == CELDA_BORRADA:
      print(f"[{i}] ")
    else:
      print(f"[{i}] ")


if __name__ == "__main__":
  tabla = HashOA(13)
  hash_insertar(tabla, "juan", 50)
  hash_insertar(tabla, "ana", 23)
  hash_insertar(tabla, "luis", 19)
  hash_insertar(tabla, "pedro", 90)
  hash_insertar(tabla, "maria", 41)

  print("Tabla despues de insertar:")
  hash_imprimir(tabla)

  resultado = hash_buscar(tabla, "pedro")
  print("Buscar 'pedro':", "encontrado" if resultado else "no encontrado")

  hash_eliminar(tabla, "pedro")

  resultado = hash_buscar(tabla, "pedro")
  print("Buscar 'pedro' luego de borrar:", "encontrado" if resultado else "no encontrado")

  print("Tabla final:")
  hash_imprimir(tabla)