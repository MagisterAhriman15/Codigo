def agregar_arista_dirigida(g, u, v):
  g[u].append((v, 1))

def dfs_topo(g, u, color, stack):
  color[u] = 1
  for v, _ in g[u]:
    if color[v] == 0:
      if not dfs_topo(g, v, color, stack):
        return False
    elif color[v] == 1:
      return False
  color[u] = 2
  stack.append(u)
  return True

def orden_topologico_dfs(g):
  color = {v: 0 for v in g}
  stack = []
  for u in g:
    if color[u] == 0:
      if not dfs_topo(g, u, color, stack):
        return None
  stack.reverse()
  return stack

def main():
  g = {i: [] for i in range(6)}
  agregar_arista_dirigida(g, 0, 2)
  agregar_arista_dirigida(g, 0, 3)
  agregar_arista_dirigida(g, 1, 3)
  agregar_arista_dirigida(g, 1, 4)
  agregar_arista_dirigida(g, 3, 5)
  agregar_arista_dirigida(g, 2, 5)

  orden = orden_topologico_dfs(g)
  if orden is None:
    print("Hay un ciclo dirigido, no existe orden topologico.")
  else:
    print("Orden topologico (DFS):")
    print(" ".join(map(str, orden)))

if __name__ == "__main__":
  main()