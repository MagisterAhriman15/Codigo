class BTreeNode:
  def __init__(self, orden, es_hoja):
    self.claves = []
    self.hijos = []
    self.cuenta = 0
    self.es_hoja = es_hoja
    self.orden = orden

def dividir_hijo(padre, idx, hijo):
  t = hijo.orden
  nuevo = BTreeNode(t, hijo.es_hoja)
  clave_media = hijo.claves[t - 1]
  nuevo.claves = hijo.claves[t:]
  if not hijo.es_hoja:
    nuevo.hijos = hijo.hijos[t:]
  hijo.claves = hijo.claves[:t - 1]
  if not hijo.es_hoja:
    hijo.hijos = hijo.hijos[:t]
  hijo.cuenta = len(hijo.claves)
  nuevo.cuenta = len(nuevo.claves)
  padre.hijos.insert(idx + 1, nuevo)
  padre.claves.insert(idx, clave_media)
  padre.cuenta = len(padre.claves)

def insertar_no_lleno(nodo, clave):
  i = nodo.cuenta - 1
  if nodo.es_hoja:
    nodo.claves.append(0)
    while i >= 0 and clave < nodo.claves[i]:
      nodo.claves[i + 1] = nodo.claves[i]
      i -= 1
    nodo.claves[i + 1] = clave
    nodo.cuenta += 1
  else:
    while i >= 0 and clave < nodo.claves[i]:
      i -= 1
    i += 1
    if nodo.hijos[i].cuenta == 2 * nodo.orden - 1:
      dividir_hijo(nodo, i, nodo.hijos[i])
      if clave > nodo.claves[i]:
        i += 1
    insertar_no_lleno(nodo.hijos[i], clave)

def btree_insertar(raiz, clave, orden):
  if raiz is None:
    raiz = BTreeNode(orden, True)
  if raiz.cuenta == 2 * raiz.orden - 1:
    nueva = BTreeNode(raiz.orden, False)
    nueva.hijos.append(raiz)
    dividir_hijo(nueva, 0, raiz)
    raiz = nueva
  insertar_no_lleno(raiz, clave)
  return raiz

def imprimir_btree(nodo, nivel=0):
  if nodo is None:
    return
  for i, clave in enumerate(nodo.claves):
    if not nodo.es_hoja:
      imprimir_btree(nodo.hijos[i], nivel + 1)
    print("  " * nivel + str(clave))
  if not nodo.es_hoja:
    imprimir_btree(nodo.hijos[len(nodo.claves)], nivel + 1)

if __name__ == "__main__":
  t = 3
  raiz = None
  datos = [10, 20, 5, 6, 12, 30, 7, 17]
  for valor in datos:
    raiz = btree_insertar(raiz, valor, t)
  print(f"Inserciones completadas con t={t}")
  print("Recorrido in-order por niveles:")
  imprimir_btree(raiz)