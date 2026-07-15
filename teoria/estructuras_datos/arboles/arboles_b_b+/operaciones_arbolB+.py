ORDEN = 3
MAX_CLAVES = 2 * ORDEN - 1

class BPlusNode:
  def __init__(self, es_hoja):
    self.claves = []
    self.hijos = []
    self.siguiente = None
    self.cuenta = 0
    self.es_hoja = es_hoja

def crear_nodo(es_hoja):
  return BPlusNode(es_hoja)

def buscar_posicion(nodo, clave):
  i = 0
  while i < nodo.cuenta and clave > nodo.claves[i]:
    i += 1
  return i

def split_hoja(padre, idx, hijo):
  nuevo = crear_nodo(True)
  mid = hijo.cuenta // 2
  nuevo.claves = hijo.claves[mid:]
  hijo.claves = hijo.claves[:mid]
  hijo.cuenta = len(hijo.claves)
  nuevo.cuenta = len(nuevo.claves)

  nuevo.siguiente = hijo.siguiente
  hijo.siguiente = nuevo

  padre.hijos.insert(idx + 1, nuevo)
  padre.claves.insert(idx, nuevo.claves[0])
  padre.cuenta = len(padre.claves)

def split_interno(padre, idx, hijo):
  nuevo = crear_nodo(False)
  mid = hijo.cuenta // 2
  promover = hijo.claves[mid]

  nuevo.claves = hijo.claves[mid + 1:]
  nuevo.hijos = hijo.hijos[mid + 1:]
  nuevo.cuenta = len(nuevo.claves)

  hijo.claves = hijo.claves[:mid]
  hijo.hijos = hijo.hijos[:mid + 1]
  hijo.cuenta = len(hijo.claves)

  padre.hijos.insert(idx + 1, nuevo)
  padre.claves.insert(idx, promover)
  padre.cuenta = len(padre.claves)

def insertar_no_lleno(nodo, clave):
  pos = buscar_posicion(nodo, clave)
  if nodo.es_hoja:
    nodo.claves.insert(pos, clave)
    nodo.cuenta += 1
  else:
    hijo = nodo.hijos[pos]
    if hijo.cuenta == MAX_CLAVES:
      if hijo.es_hoja:
        split_hoja(nodo, pos, hijo)
      else:
        split_interno(nodo, pos, hijo)
      if clave >= nodo.claves[pos]:
        pos += 1
      hijo = nodo.hijos[pos]
    insertar_no_lleno(hijo, clave)

def bplus_insertar(raiz, clave):
  if raiz is None:
    raiz = crear_nodo(True)
    raiz.claves = [clave]
    raiz.cuenta = 1
    return raiz
  if raiz.cuenta == MAX_CLAVES:
    nueva = crear_nodo(False)
    nueva.hijos.append(raiz)
    if raiz.es_hoja:
      split_hoja(nueva, 0, raiz)
    else:
      split_interno(nueva, 0, raiz)
    raiz = nueva
  insertar_no_lleno(raiz, clave)
  return raiz

def bplus_buscar(nodo, clave):
  if nodo is None:
    return False
  pos = buscar_posicion(nodo, clave)
  if nodo.es_hoja:
    return pos < nodo.cuenta and nodo.claves[pos] == clave
  return bplus_buscar(nodo.hijos[pos], clave)

def imprimir_hojas(raiz):
  if raiz is None:
    return
  while not raiz.es_hoja:
    raiz = raiz.hijos[0]
  print("Hojas enlazadas:")
  actual = raiz
  while actual:
    print("[" + ", ".join(str(x) for x in actual.claves) + "] -> ", end="")
    actual = actual.siguiente
  print("NULL")

if __name__ == "__main__":
  datos = [10, 20, 5, 6, 12, 30, 7, 17, 3, 4, 15, 25, 27]
  raiz = None
  for valor in datos:
    raiz = bplus_insertar(raiz, valor)

  imprimir_hojas(raiz)

  consultas = [6, 22, 27]
  for clave in consultas:
    print(f"Buscar {clave} -> {'encontrado' if bplus_buscar(raiz, clave) else 'no'}")