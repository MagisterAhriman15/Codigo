INF = 10**9

def agregar_arista_dirigida(g, u, v, w):
  g[u].append((v, w))

def dijkstra(g, origen):
  dist = {v: INF for v in g}
  padre = {v: None for v in g}
  visitado = {v: False for v in g}
  dist[origen] = 0

  for _ in range(len(g)):
    v_min = None
    for v in g:
      if not visitado[v] and (v_min is None or dist[v] < dist[v_min]):
        v_min = v
    if v_min is None or dist[v_min] == INF:
      break
    visitado[v_min] = True
    for u, w in g[v_min]:
      if dist[v_min] + w < dist[u]:
        dist[u] = dist[v_min] + w
        padre[u] = v_min
  return dist, padre

def reconstruir_camino(padre, origen, destino):
  camino = []
  v = destino
  while v is not None:
    camino.append(v)
    if v == origen:
      break
    v = padre[v]
  if not camino or camino[-1] != origen:
    return None
  camino.reverse()
  return camino

def main():
  g = {i: [] for i in range(6)}
  agregar_arista_dirigida(g, 0, 1, 2)
  agregar_arista_dirigida(g, 0, 2, 4)
  agregar_arista_dirigida(g, 1, 2, 1)
  agregar_arista_dirigida(g, 1, 3, 7)
  agregar_arista_dirigida(g, 2, 4, 3)
  agregar_arista_dirigida(g, 4, 3, 2)
  agregar_arista_dirigida(g, 3, 5, 1)
  agregar_arista_dirigida(g, 4, 5, 5)

  origen, destino = 0, 5
  dist, padre = dijkstra(g, origen)

  print(f"Distancias minimas desde {origen}:")
  for v in sorted(dist.keys()):
    if dist[v] == INF:
      print(f"Nodo {v}: INF")
    else:
      print(f"Nodo {v}: {dist[v]}")

  print(f"\nCamino minimo desde {origen} hasta {destino}: ", end="")
  camino = reconstruir_camino(padre, origen, destino)
  if camino is None:
    print("no existe")
  else:
    print(" -> ".join(map(str, camino)))

if __name__ == "__main__":
  main()