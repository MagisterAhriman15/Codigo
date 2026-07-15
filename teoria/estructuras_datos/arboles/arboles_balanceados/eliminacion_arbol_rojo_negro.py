ROJO = "ROJO"
NEGRO = "NEGRO"

class RbNode:
  def __init__(self, clave, color=ROJO, padre=None, nil=None):
    self.clave = clave
    self.color = color
    self.izq = nil
    self.der = nil
    self.padre = padre if padre else nil

def crear_nodo(clave, padre, nil):
  return RbNode(clave, ROJO, padre, nil)

def rotar_izquierda(raiz_ref, x, nil):
  y = x.der
  x.der = y.izq
  if y.izq != nil:
    y.izq.padre = x
  y.padre = x.padre
  if x.padre == nil:
    raiz_ref[0] = y
  elif x == x.padre.izq:
    x.padre.izq = y
  else:
    x.padre.der = y
  y.izq = x
  x.padre = y

def rotar_derecha(raiz_ref, y, nil):
  x = y.izq
  y.izq = x.der
  if x.der != nil:
    x.der.padre = y
  x.padre = y.padre
  if y.padre == nil:
    raiz_ref[0] = x
  elif y == y.padre.izq:
    y.padre.izq = x
  else:
    y.padre.der = x
  x.der = y
  y.padre = x

def arreglar_insercion(raiz_ref, n, nil):
  while n.padre != nil and n.padre.color == ROJO:
    p = n.padre
    g = p.padre
    p_es_izq = (p == g.izq)
    opuesto = g.der if p_es_izq else g.izq

    if opuesto.color == ROJO:
      p.color = NEGRO
      opuesto.color = NEGRO
      g.color = ROJO
      n = g
      continue

    if p_es_izq and n == p.der:
      rotar_izquierda(raiz_ref, p, nil)
      n = p
      p = n.padre
    elif not p_es_izq and n == p.izq:
      rotar_derecha(raiz_ref, p, nil)
      n = p
      p = n.padre

    p.color = NEGRO
    g.color = ROJO
    if p_es_izq:
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
      cur = cur.izq
    elif clave > cur.clave:
      cur = cur.der
    else:
      return raiz

  nuevo = crear_nodo(clave, padre, nil)
  if padre == nil:
    raiz = nuevo
  elif clave < padre.clave:
    padre.izq = nuevo
  else:
    padre.der = nuevo

  raiz_ref = [raiz]
  arreglar_insercion(raiz_ref, nuevo, nil)
  return raiz_ref[0]

def minimo(nodo, nil):
  while nodo.izq != nil:
    nodo = nodo.izq
  return nodo

def trasplantar(raiz_ref, u, v, nil):
  if u.padre == nil:
    raiz_ref[0] = v
  elif u == u.padre.izq:
    u.padre.izq = v
  else:
    u.padre.der = v
  v.padre = u.padre

def arreglar_eliminacion(raiz_ref, x, nil):
  while x != raiz_ref[0] and x.color == NEGRO:
    x_es_izq = (x == x.padre.izq)
    h = x.padre.der if x_es_izq else x.padre.izq

    if h.color == ROJO:
      h.color = NEGRO
      x.padre.color = ROJO
      if x_es_izq:
        rotar_izquierda(raiz_ref, x.padre, nil)
      else:
        rotar_derecha(raiz_ref, x.padre, nil)
      h = x.padre.der if x_es_izq else x.padre.izq

    if h.izq.color == NEGRO and h.der.color == NEGRO:
      h.color = ROJO
      x = x.padre
    else:
      if x_es_izq and h.der.color == NEGRO:
        h.izq.color = NEGRO
        h.color = ROJO
        rotar_derecha(raiz_ref, h, nil)
        h = x.padre.der
      elif not x_es_izq and h.izq.color == NEGRO:
        h.der.color = NEGRO
        h.color = ROJO
        rotar_izquierda(raiz_ref, h, nil)
        h = x.padre.izq
      h.color = x.padre.color
      x.padre.color = NEGRO
      if x_es_izq:
        h.der.color = NEGRO
        rotar_izquierda(raiz_ref, x.padre, nil)
      else:
        h.izq.color = NEGRO
        rotar_derecha(raiz_ref, x.padre, nil)
      x = raiz_ref[0]
  x.color = NEGRO

def buscar(nodo, clave, nil):
  while nodo != nil and clave != nodo.clave:
    nodo = nodo.izq if clave < nodo.clave else nodo.der
  return nodo

def eliminar(raiz, clave, nil):
  z = buscar(raiz, clave, nil)
  if z == nil:
    return raiz

  y = z
  y_color = y.color
  x = nil

  if z.izq == nil:
    x = z.der
    raiz_ref = [raiz]
    trasplantar(raiz_ref, z, z.der, nil)
    raiz = raiz_ref[0]
  elif z.der == nil:
    x = z.izq
    raiz_ref = [raiz]
    trasplantar(raiz_ref, z, z.izq, nil)
    raiz = raiz_ref[0]
  else:
    y = minimo(z.der, nil)
    y_color = y.color
    x = y.der
    raiz_ref = [raiz]
    if y.padre == z:
      x.padre = y
    else:
      trasplantar(raiz_ref, y, y.der, nil)
      y.der = z.der
      y.der.padre = y
    trasplantar(raiz_ref, z, y, nil)
    y.izq = z.izq
    y.izq.padre = y
    y.color = z.color
    raiz = raiz_ref[0]

  if y_color == NEGRO:
    raiz_ref = [raiz]
    arreglar_eliminacion(raiz_ref, x, nil)
    raiz = raiz_ref[0]

  return raiz

def imprimir(nodo, nivel, nil):
  if nodo == nil:
    return
  imprimir(nodo.der, nivel + 1, nil)
  print("   " * nivel + f"{nodo.clave}({'R' if nodo.color == ROJO else 'N'})")
  imprimir(nodo.izq, nivel + 1, nil)

if __name__ == "__main__":
  nil = RbNode(0, NEGRO)
  nil.izq = nil
  nil.der = nil
  nil.padre = nil

  raiz = nil
  datos = [20, 15, 25, 10, 18, 22, 30, 5, 12, 17, 19]
  for clave in datos:
    raiz = insertar(raiz, clave, nil)

  print("Inicial:")
  imprimir(raiz, 0, nil)

  borrar = [10, 22, 20]
  for clave in borrar:
    raiz = eliminar(raiz, clave, nil)
    print(f"\\nTras eliminar {clave}:")
    imprimir(raiz, 0, nil)