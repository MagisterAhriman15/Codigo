def crear_grafo(n, es_dirigido, es_ponderado):
  return {
    "n": n,
    "es_dirigido": es_dirigido,
    "es_ponderado": es_ponderado,
    "listas": {i: [] for i in range(n)}
  }

def insertar_arista(g, u, v, peso):
  g["listas"][u].append((v, peso))

def existe_arista(g, u, v):
  return any(dest == v for dest, _ in g["listas"][u])

def agregar(g, u, v, peso):
  insertar_arista(g, u, v, peso)
  if not g["es_dirigido"]:
    insertar_arista(g, v, u, peso)

def imprimir(g):
  for u in range(g["n"]):
    vecinos = " ".join(f"{v}(peso={p})" for v, p in g["listas"][u])
    print(f"{u}: {vecinos}")

def cargar_desde_archivo(ruta):
  with open(ruta, "r", encoding="utf-8") as f:
    cabecera = f.readline().strip().split()
    if len(cabecera) != 4:
      raise ValueError("Cabecera invalida")
    n, m, dirigido, ponderado = map(int, cabecera)
    g = crear_grafo(n, bool(dirigido), bool(ponderado))

    linea_actual = 1
    for linea in f:
      linea_actual += 1
      if not linea.strip():
        continue
      partes = linea.split()
      esperados = 3 if ponderado else 2
      if len(partes) != esperados:
        print(f"Linea {linea_actual} invalida: {linea.strip()}")
        continue
      u, v = map(int, partes[:2])
      peso = int(partes[2]) if ponderado else 1
      if u < 0 or u >= n or v < 0 or v >= n:
        print(f"Vertices fuera de rango en linea {linea_actual}")
        continue
      if u == v:
        print(f"Se omite lazo en linea {linea_actual}")
        continue
      if existe_arista(g, u, v):
        print(f"Arista duplicada en linea {linea_actual}")
        continue
      agregar(g, u, v, peso)
      if linea_actual - 1 >= m + 1:
        break
    return g

def main():
  try:
    g = cargar_desde_archivo("grafo.txt")
  except (OSError, ValueError) as error:
    print(f"No se pudo cargar el archivo: {error}")
    return
  print("Grafo cargado:")
  imprimir(g)

if __name__ == "__main__":
  main()