N = 9


def es_valido(tablero, fila, col, valor):
  for i in range(N):
    if tablero[fila][i] == valor or tablero[i][col] == valor:
      return False
  sf = (fila // 3) * 3
  sc = (col // 3) * 3
  for i in range(3):
    for j in range(3):
      if tablero[sf + i][sc + j] == valor:
        return False
  return True


def siguiente_vacio(tablero):
  for i in range(N):
    for j in range(N):
      if tablero[i][j] == 0:
        return i, j
  return None


def candidatos_para(tablero, fila, col):
  return [v for v in range(1, 10) if es_valido(tablero, fila, col, v)]


def resolver(tablero):
  pila = []
  while True:
    pos = siguiente_vacio(tablero)
    if pos is None:
      return True
    fila, col = pos
    candidatos = candidatos_para(tablero, fila, col)
    if candidatos:
      valor = candidatos[0]
      tablero[fila][col] = valor
      pila.append({"fila": fila, "col": col, "candidatos": candidatos, "idx": 1})
      continue

    avanzo = False
    while pila and not avanzo:
      estado = pila.pop()
      tablero[estado["fila"]][estado["col"]] = 0
      while estado["idx"] < len(estado["candidatos"]):
        valor = estado["candidatos"][estado["idx"]]
        estado["idx"] += 1
        if es_valido(tablero, estado["fila"], estado["col"], valor):
          tablero[estado["fila"]][estado["col"]] = valor
          pila.append(estado)
          avanzo = True
          break
    if not avanzo:
      return False


def imprimir(tablero):
  for fila in tablero:
    print(" ".join(str(v) for v in fila))


if __name__ == "__main__":
  tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
  ]

  if resolver(tablero):
    print("Sudoku resuelto:")
    imprimir(tablero)
  else:
    print("Sin solucion")