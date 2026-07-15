ROJO = "ROJO"
NEGRO = "NEGRO"

class RbNode:
  def __init__(self, clave, color=ROJO, padre=None, nil=None):
    self.clave = clave
    self.color = color
    self.izquierdo = nil
    self.derecho = nil
    self.padre = padre if padre else nil

def crear_nodo(clave, padre, nil):
  return RbNode(clave, ROJO, padre, nil)

def rotar_izquierda(raiz_ref, x, nil):
  y = x.derecho
  x.derecho = y.izquierdo
  if y.izquierdo != nil:
    y.izquierdo.padre = x
  y.padre = x.padre
  if x.padre == nil:
    raiz_ref[0] = y
  elif x == x.padre.izquierdo:
    x.padre.izquierdo = y
  else:
    x.padre.derecho = y
  y.izquierdo = x
  x.padre = y

def rotar_derecha(raiz_ref, y, nil):
  x = y.izquierdo
  y.izquierdo = x.derecho
  if x.derecho != nil:
    x.derecho.padre = y
  x.padre = y.padre
  if y.padre == nil:
    raiz_ref[0] = x
  elif y == y.padre.izquierdo:
    y.padre.izquierdo = x
  else:
    y.padre.derecho = x
  x.derecho = y
  y.padre = x

def arreglar_insercion(raiz_ref, n, nil):
  while n.padre != nil and n.padre.color == ROJO:
    p = n.padre
    g = p.padre
    padre_es_izq = (p == g.izquierdo)
    tio = g.derecho if padre_es_izq else g.izquierdo

    if tio.color == ROJO:
      p.color = NEGRO
      tio.color = NEGRO
      g.color = ROJO
      n = g
      continue

    if padre_es_izq and n == p.derecho:
      rotar_izquierda(raiz_ref, p, nil)
      n = p
      p = n.padre
    elif not padre_es_izq and n == p.izquierdo:
      rotar_derecha(raiz_ref, p, nil)
      n = p
      p = n.padre

    p.color = NEGRO
    g.color = ROJO
    if padre_es_izq:
      rotar_derecha(raiz_ref, g, nil)
    else:
      rotar_izquierda(raiz_ref, g, nil)
  raiz_ref[0].color = NEGRO

def insertar(raiz, clave, nil):
  padre = nil
  cur = raiz
  while cur != nil:
    padre = cur
    if clave < cur.clave:
      cur = cur.izquierdo
    elif clave > cur.clave:
      cur = cur.derecho
    else:
      return raiz

  nuevo = crear_nodo(clave, padre, nil)
  if padre == nil:
    raiz = nuevo
  elif clave < padre.clave:
    padre.izquierdo = nuevo
  else:
    padre.derecho = nuevo

  raiz_ref = [raiz]
  arreglar_insercion(raiz_ref, nuevo, nil)
  return raiz_ref[0]

def imprimir_en_orden(n, nil):
  if n == nil:
    return
  imprimir_en_orden(n.izquierdo, nil)
  color = "R" if n.color == ROJO else "N"
  print(f"{n.clave}({color})", end=" ")
  imprimir_en_orden(n.derecho, nil)

if __name__ == "__main__":
  nil = RbNode(0, NEGRO)
  nil.izquierdo = nil
  nil.derecho = nil
  nil.padre = nil

  raiz = nil
  datos = [10, 20, 30, 15, 25, 5, 1, 50]
  for clave in datos:
    raiz = insertar(raiz, clave, nil)

  imprimir_en_orden(raiz, nil)
  print()