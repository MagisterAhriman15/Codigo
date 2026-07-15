class AvlNode:
  def __init__(self, clave):
    self.clave = clave
    self.altura = 0
    self.izquierdo = None
    self.derecho = None

def altura_nodo_avl(nodo):
  return nodo.altura if nodo else -1

def actualizar_altura(nodo):
  if not nodo:
    return
  h_izq = altura_nodo_avl(nodo.izquierdo)
  h_der = altura_nodo_avl(nodo.derecho)
  nodo.altura = 1 + max(h_izq, h_der)

def factor_balance_avl(nodo):
  if not nodo:
    return 0
  return altura_nodo_avl(nodo.izquierdo) - altura_nodo_avl(nodo.derecho)

def crear_nodo_avl(clave):
  return AvlNode(clave)

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

def insertar_avl(nodo, clave):
  if not nodo:
    return crear_nodo_avl(clave)
  if clave < nodo.clave:
    nodo.izquierdo = insertar_avl(nodo.izquierdo, clave)
  elif clave > nodo.clave:
    nodo.derecho = insertar_avl(nodo.derecho, clave)
  else:
    return nodo

  actualizar_altura(nodo)
  fb = factor_balance_avl(nodo)

  if fb > 1 and clave < nodo.izquierdo.clave:  # LL
    return rotar_derecha(nodo)
  if fb < -1 and clave > nodo.derecho.clave:  # RR
    return rotar_izquierda(nodo)
  if fb > 1 and clave > nodo.izquierdo.clave:  # LR
    nodo.izquierdo = rotar_izquierda(nodo.izquierdo)
    return rotar_derecha(nodo)
  if fb < -1 and clave < nodo.derecho.clave:  # RL
    nodo.derecho = rotar_derecha(nodo.derecho)
    return rotar_izquierda(nodo)
  return nodo

def imprimir_inorden(nodo):
  if not nodo:
    return
  imprimir_inorden(nodo.izquierdo)
  print(nodo.clave, end=" ")
  imprimir_inorden(nodo.derecho)

if __name__ == "__main__":
  claves = [30, 20, 40, 10, 25, 50, 5, 35]
  raiz = None

  for clave in claves:
    raiz = insertar_avl(raiz, clave)

  print("AVL en inorden:", end=" ")
  imprimir_inorden(raiz)
  print()