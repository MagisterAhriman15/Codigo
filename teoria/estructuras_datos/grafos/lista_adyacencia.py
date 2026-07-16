def crear_grafo_lista(n):
  return {i: [] for i in range(n)}

def agregar_arista(g, u, v, peso=1, es_dirigido=False):
  if u not in g or v not in g:
    return
  g[u].append((v, peso))
  if not es_dirigido:
    g[v].append((u, peso))

def eliminar_arista(g, u, v, es_dirigido=False):
  if u not in g or v not in g:
    return
  g[u] = [(dest, peso) for dest, peso in g[u] if dest != v]
  if not es_dirigido:
    g[v] = [(dest, peso) for dest, peso in g[v] if dest != u]

def imprimir_grafo(g):
  for u in sorted(g.keys()):
    vecinos = " ".join(f"{v}(peso={p})" for v, p in g[u])
    print(f"{u}: {vecinos}")

def main():
  g = crear_grafo_lista(4)
  agregar_arista(g, 0, 1, 3, False)
  agregar_arista(g, 0, 3, 1, False)
  agregar_arista(g, 1, 2, 2, False)
  agregar_arista(g, 3, 2, 4, False)
  eliminar_arista(g, 0, 1, False)

  imprimir_grafo(g)

if __name__ == "__main__":
  main()