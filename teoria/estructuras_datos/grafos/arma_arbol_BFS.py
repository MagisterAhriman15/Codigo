from collections import deque

def agregar_arista(g, u, v):
  g[u].append((v, 1))
  g[v].append((u, 1))

def imprimir_arbol_bfs(g, origen):
  padre = {v: None for v in g}
  nivel = {v: -1 for v in g}
  cola = deque([origen])
  padre[origen] = origen
  nivel[origen] = 0

  print(f"Arbol BFS (origen {origen}):")
  while cola:
    u = cola.popleft()
    for v, _ in g[u]:
      if padre[v] is None:
        padre[v] = u
        nivel[v] = nivel[u] + 1
        print(f"{u} -- {v} (nivel {nivel[v]})")
        cola.append(v)

def main():
  g = {i: [] for i in range(6)}
  agregar_arista(g, 0, 1)
  agregar_arista(g, 0, 2)
  agregar_arista(g, 1, 3)
  agregar_arista(g, 1, 4)
  agregar_arista(g, 2, 5)

  imprimir_arbol_bfs(g, 0)

if __name__ == "__main__":
  main()