def agregar_arista(g, u, v):
  g[u].append((v, 1))
  g[v].append((u, 1))

def dfs_puentes(g, u, padre, visitado, tin, low, timer, puentes):
  visitado[u] = True
  tin[u] = low[u] = timer[0]
  timer[0] += 1

  for v, _ in g[u]:
    if v == padre:
      continue
    if not visitado[v]:
      dfs_puentes(g, v, u, visitado, tin, low, timer, puentes)
      if low[v] > tin[u]:
        puentes.append((u, v))
      low[u] = min(low[u], low[v])
    else:
      low[u] = min(low[u], tin[v])

def encontrar_puentes(g):
  visitado = {v: False for v in g}
  tin = {v: -1 for v in g}
  low = {v: -1 for v in g}
  timer = [0]
  puentes = []

  for u in g:
    if not visitado[u]:
      dfs_puentes(g, u, None, visitado, tin, low, timer, puentes)
  return puentes

def main():
  g = {i: [] for i in range(7)}
  agregar_arista(g, 0, 1)
  agregar_arista(g, 1, 2)
  agregar_arista(g, 2, 0)
  agregar_arista(g, 1, 3)  # puente
  agregar_arista(g, 3, 4)
  agregar_arista(g, 4, 5)
  agregar_arista(g, 5, 3)  # ciclo 3-4-5
  agregar_arista(g, 4, 6)  # puente

  print("Puentes del grafo:")
  for u, v in encontrar_puentes(g):
    print(f"Puente: {u} -- {v}")

if __name__ == "__main__":
  main()