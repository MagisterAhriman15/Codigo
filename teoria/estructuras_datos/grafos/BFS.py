from collections import deque

def bfs_con_padres(g, origen):
  visitado = {v: False for v in g}
  padre = {v: None for v in g}
  cola = deque([origen])
  visitado[origen] = True

  while cola:
    u = cola.popleft()
    for v, _ in g[u]:
      if not visitado[v]:
        visitado[v] = True
        padre[v] = u
        cola.append(v)
  return padre

def reconstruir_camino(padre, origen, destino):
  camino = []
  actual = destino
  while actual is not None:
    camino.append(actual)
    if actual == origen:
      break
    actual = padre[actual]
  if not camino or camino[-1] != origen:
    print(f"No hay camino de {origen} a {destino}")
    return
  camino.reverse()
  print(f"Camino {origen} -> {destino}: " + " -> ".join(map(str, camino)))

def main():
  g = {
    0: [(1, 1), (2, 1)],
    1: [(0, 1), (3, 1)],
    2: [(0, 1), (3, 1)],
    3: [(1, 1), (2, 1), (4, 1)],
    4: [(3, 1)]
  }

  padre = bfs_con_padres(g, 0)
  print("Padres en el arbol BFS desde 0:")
  for v in sorted(padre.keys()):
    print(f"{v} -> {padre[v] if padre[v] is not None else -1}")

  reconstruir_camino(padre, 0, 4)

if __name__ == "__main__":
  main()