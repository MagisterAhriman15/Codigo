MOVS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def resolver(mapa):
  filas, cols = len(mapa), len(mapa[0])
  visitado = [[False] * cols for _ in range(filas)]

  inicio = None
  for i, fila in enumerate(mapa):
    for j, ch in enumerate(fila):
      if ch == "S":
        inicio = (i, j)
        break
    if inicio:
      break

  if inicio is None:
    return False

  pila = [inicio]
  visitado[inicio[0]][inicio[1]] = True

  while pila:
    fila, col = pila[-1]
    if mapa[fila][col] == "E":
      return True

    avanzo = False
    for df, dc in MOVS:
      nf, nc = fila + df, col + dc
      if not (0 <= nf < filas and 0 <= nc < cols):
        continue
      if mapa[nf][nc] == "#" or visitado[nf][nc]:
        continue
      visitado[nf][nc] = True
      pila.append((nf, nc))
      avanzo = True
      break

    if not avanzo:
      pila.pop()

  return False


if __name__ == "__main__":
  lab = [
    "S....#..",
    "##.#.#..",
    "..#....E",
    "..#....#",
    "..#####.",
    "..#.....",
    "..###.##",
    "........",
  ]

  print("Resultado:", "Camino encontrado" if resolver(lab) else "Sin salida")