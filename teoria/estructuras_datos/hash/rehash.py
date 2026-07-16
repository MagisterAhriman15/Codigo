class HashNode:
  def __init__(self, clave, valor, sig=None):
    self.clave = clave
    self.valor = valor
    self.sig = sig


class HashTable:
  def __init__(self, capacidad):
    self.capacidad = capacidad
    self.cantidad = 0
    self.buckets = [None] * capacidad


def hash_cadena(clave, cap):
  h = 5381
  for caracter in clave:
    h = ((h << 5) + h) + ord(caracter)
  return h % cap


def hash_insertar(tabla, clave, valor):
  idx = hash_cadena(clave, tabla.capacidad)
  nodo = tabla.buckets[idx]
  while nodo is not None:
    if nodo.clave == clave:
      nodo.valor = valor
      return True
    nodo = nodo.sig
  tabla.buckets[idx] = HashNode(clave, valor, tabla.buckets[idx])
  tabla.cantidad += 1
  return True


def hash_rehash(tabla, nueva_capacidad):
  nuevos_buckets = [None] * nueva_capacidad
  destino = HashTable(nueva_capacidad)
  destino.buckets = nuevos_buckets

  for bucket in tabla.buckets:
    nodo = bucket
    while nodo is not None:
      sig = nodo.sig
      idx = hash_cadena(nodo.clave, destino.capacidad)
      destino.buckets[idx] = HashNode(nodo.clave, nodo.valor, destino.buckets[idx])
      destino.cantidad += 1
      nodo = sig

  tabla.buckets = nuevos_buckets
  tabla.capacidad = nueva_capacidad
  tabla.cantidad = destino.cantidad
  return True


def hash_imprimir(tabla):
  for i in range(tabla.capacidad):
    partes = []
    nodo = tabla.buckets[i]
    while nodo is not None:
      partes.append(f"({nodo.clave} -> {nodo.valor})")
      nodo = nodo.sig
    print(f"[{i}]: " + " ".join(partes))


if __name__ == "__main__":
  tabla = HashTable(4)
  claves = ["juan", "ana", "luis", "pedro", "maria", "sofia"]
  valores = [50, 23, 19, 90, 41, 77]

  for i in range(len(claves)):
    alpha = (tabla.cantidad + 1) / tabla.capacidad
    if alpha >= 1.0:
      nueva = tabla.capacidad * 2 + 1
      print(f"Rehash a capacidad {nueva} (alpha previsto {alpha:.2f})")
      hash_rehash(tabla, nueva)
    hash_insertar(tabla, claves[i], valores[i])

  print("Tabla final:")
  hash_imprimir(tabla)

  hash_rehash(tabla, tabla.capacidad * 2 + 1)
  print("Tras rehash manual:")
  hash_imprimir(tabla)