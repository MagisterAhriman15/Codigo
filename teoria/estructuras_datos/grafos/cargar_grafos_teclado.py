MAX_V = 100

def crear_grafo(n, es_dirigido, es_ponderado):
  return {
    "n": n,
    "es_dirigido": es_dirigido,
    "es_ponderado": es_ponderado,
    "listas": {i: [] for i in range(n)}
  }

def insertar_arista(g, u, v, peso):
  g["listas"][u].append((v, peso))

def agregar(g, u, v, peso):
  insertar_arista(g, u, v, peso)
  if not g["es_dirigido"]:
    insertar_arista(g, v, u, peso)

def existe_arista(g, u, v):
  return any(dest == v for dest, _ in g["listas"][u])

def imprimir(g):
  for u in range(g["n"]):
    vecinos = " ".join(f"{v}(peso={p})" for v, p in g["listas"][u])
    print(f"{u}: {vecinos}")

def leer_entero(mensaje):
  try:
    return int(input(mensaje))
  except ValueError:
    return None

def main():
  n = leer_entero(f"Cantidad de vertices (max {MAX_V}): ")
  if n is None or n <= 0 or n > MAX_V:
    print("Valor de vertices invalido")
    return

  max_aristas = n * (n - 1) // 2
  m = leer_entero(f"Cantidad de aristas (0..{max_aristas}): ")
  if m is None or m < 0 or m > max_aristas:
    print("Cantidad de aristas invalida")
    return

  ponderado = True
  dirigido = False
  g = crear_grafo(n, dirigido, ponderado)

  i = 0
  while i < m:
    try:
      par = input(f"Arista {i + 1} (u v): ").split()
      if len(par) != 2:
        print("Par fuera de rango")
        continue
      u, v = map(int, par)
    except ValueError:
      print("Par fuera de rango")
      continue

    if u < 0 or u >= n or v < 0 or v >= n:
      print("Par fuera de rango")
      continue
    if u == v:
      print("No se permiten lazos en grafo simple")
      continue
    if existe_arista(g, u, v):
      print("Arista duplicada, se omite")
      continue

    peso = 1
    if ponderado:
      peso = leer_entero("Peso: ")
      if peso is None:
        print("Peso invalido")
        continue

    agregar(g, u, v, peso)
    i += 1

  print("Grafo cargado:")
  imprimir(g)

if __name__ == "__main__":
  main()