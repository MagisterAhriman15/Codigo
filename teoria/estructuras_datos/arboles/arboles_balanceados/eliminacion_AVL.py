class AvlNode:
  def __init__(self, clave):
    self.clave = clave
    self.altura = 0
    self.izquierdo = None
    self.derecho = None

def altura_nodo(nodo):
  return nodo.altura if nodo else -1

def actualizar_altura(nodo):
  if not nodo:
    return
  nodo.altura = 1 + max(altura_nodo(nodo.izquierdo), altura_nodo(nodo.derecho))

def factor_balance(nodo):
  if not nodo:
    return 0
  return altura_nodo(nodo.izquierdo) - altura_nodo(nodo.derecho)

def rotar_derecha(y):
  x = y.izquierdo
  t2 = x.derecho
  x.derecho = y
  y.izquierdo = t2
  actualizar_altura(y)
  actualizar_altura(x)
  return x

def rotar_izquierda(y):
  x = y.derecho
  t2 = x.izquierdo
  x.izquierdo = y
  y.derecho = t2
  actualizar_altura(y)
  actualizar_altura(x)
  return x

def crear_nodo(clave):
  return AvlNode(clave)

def min_nodo(nodo):
  actual = nodo
  while actual and actual.izquierdo:
    actual = actual.izquierdo
  return actual

def insertar_avl(raiz, clave):
  if not raiz:
    return crear_nodo(clave)
  if clave < raiz.clave:
    raiz.izquierdo = insertar_avl(raiz.izquierdo, clave)
  elif clave > raiz.clave:
    raiz.derecho = insertar_avl(raiz.derecho, clave)
  else:
    return raiz

  actualizar_altura(raiz)
  fb = factor_balance(raiz)

  if fb > 1 and clave < raiz.izquierdo.clave:  # LL
    return rotar_derecha(raiz)
  if fb < -1 and clave > raiz.derecho.clave:  # RR
    return rotar_izquierda(raiz)
  if fb > 1 and clave > raiz.izquierdo.clave:  # LR
    raiz.izquierdo = rotar_izquierda(raiz.izquierdo)
    return rotar_derecha(raiz)
  if fb < -1 and clave < raiz.derecho.clave:  # RL
    raiz.derecho = rotar_derecha(raiz.derecho)
    return rotar_izquierda(raiz)
  return raiz

def eliminar_avl(raiz, clave):
  if not raiz:
    return None

  if clave < raiz.clave:
    raiz.izquierdo = eliminar_avl(raiz.izquierdo, clave)
  elif clave > raiz.clave:
    raiz.derecho = eliminar_avl(raiz.derecho, clave)
  else:
    if not raiz.izquierdo or not raiz.derecho:
      return raiz.izquierdo if raiz.izquierdo else raiz.derecho
    succ = min_nodo(raiz.derecho)
    raiz.clave = succ.clave
    raiz.derecho = eliminar_avl(raiz.derecho, succ.clave)

  actualizar_altura(raiz)
  fb = factor_balance(raiz)

  if fb > 1 and factor_balance(raiz.izquierdo) >= 0:  # LL
    return rotar_derecha(raiz)
  if fb > 1 and factor_balance(raiz.izquierdo) < 0:  # LR
    raiz.izquierdo = rotar_izquierda(raiz.izquierdo)
    return rotar_derecha(raiz)
  if fb < -1 and factor_balance(raiz.derecho) <= 0:  # RR
    return rotar_izquierda(raiz)
  if fb < -1 and factor_balance(raiz.derecho) > 0:  # RL
    raiz.derecho = rotar_derecha(raiz.derecho)
    return rotar_izquierda(raiz)
  return raiz

def imprimir_inorden(nodo):
  if not nodo:
    return
  imprimir_inorden(nodo.izquierdo)
  print(nodo.clave, end=" ")
  imprimir_inorden(nodo.derecho)

if __name__ == "__main__":
  claves = [30, 20, 40, 10, 25, 50, 5, 35, 45]
  eliminar = [10, 40, 30]

  raiz = None
  for clave in claves:
    raiz = insertar_avl(raiz, clave)

  print("AVL inicial (inorden): ", end="")
  imprimir_inorden(raiz)
  print("\n")

  for clave in eliminar:
    raiz = eliminar_avl(raiz, clave)
    print(f"Tras eliminar {clave}: ", end="")
    imprimir_inorden(raiz)
    print()

  print("AVL final: ", end="")
  imprimir_inorden(raiz)
  print()