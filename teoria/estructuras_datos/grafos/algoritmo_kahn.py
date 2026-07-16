from collections import deque

def agregar_arista_dirigida(g, u, v):
  g[u].append((v, 1))

def orden_topologico_kahn(g):
  indeg = {v: 0 for v in g}
  for u in g:
    for v, _ in g[u]:
      indeg[v] += 1

  cola = deque([v for v in g if indeg[v] == 0])
  orden = []

  while cola:
    u = cola.popleft()
    orden.append(u)
    for v, _ in g[u]:
      indeg[v] -= 1
      if indeg[v] == 0:
        cola.append(v)

  if len(orden) != len(g):
    return None
  return orden

def main():
  g = {i: [] for i in range(6)}
  agregar_arista_dirigida(g, 0, 2)
  agregar_arista_dirigida(g, 0, 3)
  agregar_arista_dirigida(g, 1, 3)
  agregar_arista_dirigida(g, 1, 4)
  agregar_arista_dirigida(g, 3, 5)
  agregar_arista_dirigida(g, 2, 5)

  orden = orden_topologico_kahn(g)
  if orden is None:
    print("Hay un ciclo dirigido, no existe orden topologico.")
  else:
    print("Orden topologico (Kahn):")
    print(" ".join(map(str, orden)))

if __name__ == "__main__":
  main()