import random
import time

def swap(valores, i, j):
  valores[i], valores[j] = valores[j], valores[i]

def imprimir_lista(valores):
  for valor in valores:
    print(valor, end=", ")

def bubble_sort(valores):
  n = len(valores)
  for i in range(n - 1):
    hubo_intercambio = False
    limite = n - 1 - i
    for j in range(limite):
      if valores[j] > valores[j + 1]:
        swap(valores, j, j + 1)
        hubo_intercambio = True
    if not hubo_intercambio:
      break

def insertion_sort(valores):
  for i in range(1, len(valores)):
    actual = valores[i]
    j = i - 1
    while j >= 0 and valores[j] > actual:
      valores[j + 1] = valores[j]
      j -= 1
    valores[j + 1] = actual

def selection_sort(valores):
  for i in range(len(valores) - 1):
    indice_min = i
    for j in range(i + 1, len(valores)):
      if valores[j] < valores[indice_min]:
        indice_min = j
    if indice_min != i:
      swap(valores, i, indice_min)

def ejecutar(nombre, funcion, valores):
  inicio = time.perf_counter()
  funcion(valores)
  fin = time.perf_counter()
  ms = (fin - inicio) * 1000
  print(f"{nombre} -> tiempo: {ms:.3f} ms")

def main():
  max_valores = 1000
  try:
    n = int(input(f"Ingrese cantidad de elementos (max {max_valores}): "))
  except ValueError:
    print("Tamano no valido.")
    return

  if n <= 0 or n > max_valores:
    print("Tamano no valido.")
    return

  original = [random.randint(0, 999) for _ in range(n)]
  print("Antes: ", end="")
  imprimir_lista(original)
  print()

  opcion = input("Seleccione algoritmo (b)ubble, (i)nsertion, (s)election: ").strip().lower()
  trabajo = list(original)

  if opcion == "b":
    ejecutar("Bubble Sort", bubble_sort, trabajo)
  elif opcion == "i":
    ejecutar("Insertion Sort", insertion_sort, trabajo)
  elif opcion == "s":
    ejecutar("Selection Sort", selection_sort, trabajo)
  else:
    print("Opcion no reconocida.")
    return

  print("Despues: ", end="")
  imprimir_lista(trabajo)
  print()

if __name__ == "__main__":
  main()