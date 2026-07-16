from collections import deque

def agregar_arista(g, u, v):
  g[u].append((v, 1))
  g[v].append((u, 1))

def bfs_distancias(g, origen):
  dist = {v: -1 for v in g}
  padre = {v: None for v in g}
  cola = deque([origen])
  dist[origen] = 0
  padre[origen] = origen

  while cola:
    u = cola.popleft()
    for v, _ in g[u]:
      if dist[v] == -1:
        dist[v] = dist[u] + 1
        padre[v] = u
        cola.append(v)
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
  agregar_arista(g, 0, 1)
  agregar_arista(g, 0, 2)
  agregar_arista(g, 1, 3)
  agregar_arista(g, 1, 4)
  agregar_arista(g, 2, 5)

  origen, destino = 0, 5
  dist, padre = bfs_distancias(g, origen)

  print(f"Distancias minimas desde {origen}:")
  for v in sorted(dist.keys()):
    print(f"Nodo {v}: {dist[v]}")

  print(f"\nCamino minimo de {origen} a {destino}: ", end="")
  camino = reconstruir_camino(padre, origen, destino)
  if camino is None:
    print("no existe")
  else:
    print(" -> ".join(map(str, camino)))

if __name__ == "__main__":
  main()