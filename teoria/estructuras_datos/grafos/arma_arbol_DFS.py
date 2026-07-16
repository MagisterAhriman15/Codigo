def agregar_arista(g, u, v):
  g[u].append((v, 1))
  g[v].append((u, 1))

def dfs_arbol(g, u, padre, nivel, visitado):
  visitado[u] = True
  if padre is not None:
    print(f"{padre} -- {u} (nivel {nivel})")
  for v, _ in g[u]:
    if not visitado[v]:
      dfs_arbol(g, v, u, nivel + 1, visitado)

def main():
  g = {i: [] for i in range(6)}
  agregar_arista(g, 0, 1)
  agregar_arista(g, 0, 2)
  agregar_arista(g, 1, 3)
  agregar_arista(g, 1, 4)
  agregar_arista(g, 2, 5)

  visitado = {v: False for v in g}
  print("Arbol DFS (origen 0):")
  dfs_arbol(g, 0, None, 0, visitado)

if __name__ == "__main__":
  main()