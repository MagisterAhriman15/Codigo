def agregar_arista(g, u, v):
  g[u].append((v, 1))
  g[v].append((u, 1))

def dfs_articulacion(g, u, padre, visitado, tin, low, timer, es_articulacion):
  visitado[u] = True
  tin[u] = low[u] = timer[0]
  timer[0] += 1
  hijos = 0

  for v, _ in g[u]:
    if v == padre:
      continue
    if not visitado[v]:
      hijos += 1
      dfs_articulacion(g, v, u, visitado, tin, low, timer, es_articulacion)
      low[u] = min(low[u], low[v])
      if padre is not None and low[v] >= tin[u]:
        es_articulacion[u] = True
    else:
      low[u] = min(low[u], tin[v])

  if padre is None and hijos >= 2:
    es_articulacion[u] = True

def encontrar_puntos_articulacion(g):
  visitado = {v: False for v in g}
  tin = {v: -1 for v in g}
  low = {v: -1 for v in g}
  es_articulacion = {v: False for v in g}
  timer = [0]

  for u in g:
    if not visitado[u]:
      dfs_articulacion(g, u, None, visitado, tin, low, timer, es_articulacion)
  return [v for v, es in es_articulacion.items() if es]

def main():
  g = {i: [] for i in range(7)}
  agregar_arista(g, 0, 1)
  agregar_arista(g, 1, 2)
  agregar_arista(g, 2, 0)  # ciclo 0-1-2
  agregar_arista(g, 1, 3)  # 1 es articulacion
  agregar_arista(g, 3, 4)
  agregar_arista(g, 4, 5)
  agregar_arista(g, 5, 3)  # ciclo 3-4-5
  agregar_arista(g, 4, 6)  # 4 es articulacion

  print("Puntos de articulacion:")
  for v in encontrar_puntos_articulacion(g):
    print(f" - {v}")

if __name__ == "__main__":
  main()