class MatrizAdy:
  def __init__(self, n):
    self.n = n
    self.m = [[0 for _ in range(n)] for _ in range(n)]

def crear_matriz(n):
  if n <= 0:
    return None
  return MatrizAdy(n)

def insertar_arista(g, u, v, peso=1, es_dirigido=False):
  if g is None or not (0 <= u < g.n and 0 <= v < g.n):
    return
  g.m[u][v] = peso if peso != 0 else 1
  if not es_dirigido:
    g.m[v][u] = g.m[u][v]

def eliminar_arista(g, u, v, es_dirigido=False):
  if g is None or not (0 <= u < g.n and 0 <= v < g.n):
    return
  g.m[u][v] = 0
  if not es_dirigido:
    g.m[v][u] = 0

def son_adyacentes(g, u, v):
  if g is None or not (0 <= u < g.n and 0 <= v < g.n):
    return False
  return g.m[u][v] != 0

def imprimir_matriz(g):
  if g is None:
    return
  encabezado = "   " + "".join(f"{j:3d}" for j in range(g.n))
  print(encabezado)
  for i in range(g.n):
    fila = "".join(f"{g.m[i][j]:3d}" for j in range(g.n))
    print(f"{i:3d}{fila}")

def main():
  g = crear_matriz(4)
  if g is None:
    raise SystemExit("No se pudo crear la matriz")

  insertar_arista(g, 0, 1, 5, False)
  insertar_arista(g, 0, 2, 0, False)
  insertar_arista(g, 2, 3, 2, False)
  eliminar_arista(g, 0, 2, False)

  print(f"0 y 1 son adyacentes? {'si' if son_adyacentes(g, 0, 1) else 'no'}")
  imprimir_matriz(g)

if __name__ == "__main__":
  main()