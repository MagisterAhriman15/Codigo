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
    h = ((h << 5) + h) + ord(caracter)  # djb2
  return h % cap


def hash_insertar(tabla, clave, valor):
  idx = hash_cadena(clave, tabla.capacidad)
  nodo = tabla.buckets[idx]
  while nodo is not None:
    if nodo.clave == clave:
      nodo.valor = valor
      return True
    nodo = nodo.sig
  nuevo = HashNode(clave, valor, tabla.buckets[idx])
  tabla.buckets[idx] = nuevo
  tabla.cantidad += 1
  return True


def hash_buscar(tabla, clave):
  idx = hash_cadena(clave, tabla.capacidad)
  nodo = tabla.buckets[idx]
  while nodo is not None:
    if nodo.clave == clave:
      return nodo
    nodo = nodo.sig
  return None


def hash_eliminar(tabla, clave):
  idx = hash_cadena(clave, tabla.capacidad)
  actual = tabla.buckets[idx]
  anterior = None
  while actual is not None:
    if actual.clave == clave:
      if anterior is None:
        tabla.buckets[idx] = actual.sig
      else:
        anterior.sig = actual.sig
      tabla.cantidad -= 1
      return True
    anterior = actual
    actual = actual.sig
  return False


def hash_imprimir(tabla):
  for i in range(tabla.capacidad):
    partes = []
    nodo = tabla.buckets[i]
    while nodo is not None:
      partes.append(f"({nodo.clave} -> {nodo.valor})")
      nodo = nodo.sig
    print(f"[{i}]: " + " ".join(partes))


def hash_destruir(tabla):
  tabla.buckets = []
  tabla.cantidad = 0
  tabla.capacidad = 0


if __name__ == "__main__":
  tabla = HashTable(8)
  hash_insertar(tabla, "juan", 50)
  hash_insertar(tabla, "ana", 23)
  hash_insertar(tabla, "luis", 19)
  hash_insertar(tabla, "pedro", 90)
  hash_insertar(tabla, "maria", 41)

  print("Tabla final:")
  hash_imprimir(tabla)

  resultado = hash_buscar(tabla, "pedro")
  print("Buscar 'pedro':", "encontrado" if resultado else "no encontrado")

  hash_eliminar(tabla, "pedro")

  resultado = hash_buscar(tabla, "pedro")
  print("Buscar 'pedro':", "encontrado" if resultado else "no encontrado")

  hash_destruir(tabla)