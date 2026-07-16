import random
import time

def merge_with_buffer(arr, buffer, inicio, medio, fin):
  i = inicio
  j = medio + 1
  k = inicio
  while i <= medio and j <= fin:
    if arr[i] <= arr[j]:
      buffer[k] = arr[i]
      i += 1
    else:
      buffer[k] = arr[j]
      j += 1
    k += 1
  while i <= medio:
    buffer[k] = arr[i]
    i += 1
    k += 1
  while j <= fin:
    buffer[k] = arr[j]
    j += 1
    k += 1
  arr[inicio:fin + 1] = buffer[inicio:fin + 1]

def mergesort_rec(arr, buffer, inicio, fin):
  if inicio >= fin:
    return
  medio = (inicio + fin) // 2
  mergesort_rec(arr, buffer, inicio, medio)
  mergesort_rec(arr, buffer, medio + 1, fin)
  merge_with_buffer(arr, buffer, inicio, medio, fin)

def mergesort_topdown(arr):
  if not arr:
    return
  buffer = [0] * len(arr)
  mergesort_rec(arr, buffer, 0, len(arr) - 1)

def mediana_de_tres(arr, inicio, fin):
  medio = (inicio + fin) // 2
  if arr[medio] < arr[inicio]:
    arr[medio], arr[inicio] = arr[inicio], arr[medio]
  if arr[fin] < arr[inicio]:
    arr[fin], arr[inicio] = arr[inicio], arr[fin]
  if arr[fin] < arr[medio]:
    arr[fin], arr[medio] = arr[medio], arr[fin]
  return medio

def particion_lomuto_mediana(arr, inicio, fin):
  m = mediana_de_tres(arr, inicio, fin)
  arr[m], arr[fin] = arr[fin], arr[m]
  pivote = arr[fin]
  i = inicio - 1
  for j in range(inicio, fin):
    if arr[j] <= pivote:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
  return i + 1

def quicksort(arr, inicio, fin):
  if inicio >= fin:
    return
  p = particion_lomuto_mediana(arr, inicio, fin)
  quicksort(arr, inicio, p - 1)
  quicksort(arr, p + 1, fin)

def sift_down(arr, n, i):
  mayor = i
  hijo_izq = 2 * i + 1
  hijo_der = 2 * i + 2
  if hijo_izq < n and arr[hijo_izq] > arr[mayor]:
    mayor = hijo_izq
  if hijo_der < n and arr[hijo_der] > arr[mayor]:
    mayor = hijo_der
  if mayor != i:
    arr[i], arr[mayor] = arr[mayor], arr[i]
    sift_down(arr, n, mayor)

def heapify(arr):
  n = len(arr)
  for i in range((n // 2) - 1, -1, -1):
    sift_down(arr, n, i)

def heapsort(arr):
  heapify(arr)
  for fin in range(len(arr) - 1, 0, -1):
    arr[0], arr[fin] = arr[fin], arr[0]
    sift_down(arr, fin, 0)

def ejecutar_y_medir(nombre, fn, arr):
  inicio = time.perf_counter()
  fn(arr)
  fin = time.perf_counter()
  ms = (fin - inicio) * 1000.0
  print(f"{nombre} -> tiempo: {ms:.3f} ms")

def ejecutar_y_medir_rango(nombre, fn, arr):
  inicio = time.perf_counter()
  fn(arr, 0, len(arr) - 1)
  fin = time.perf_counter()
  ms = (fin - inicio) * 1000.0
  print(f"{nombre} -> tiempo: {ms:.3f} ms")

def generar_aleatorio(n, max_val):
  return [random.randint(0, max_val) for _ in range(n)]

def menu():
  max_n = 50000
  n = int(input(f"Ingrese cantidad de elementos (max {max_n}): "))
  if n <= 0 or n > max_n:
    print("Tamano no valido.")
    return

  original = generar_aleatorio(n, 100000)
  print("Antes:", original[:20], "...")

  opcion = input("Seleccione algoritmo (m)erge, (q)uick, (h)eap: ").strip().lower()
  trabajo = list(original)

  if opcion == "m":
    ejecutar_y_medir("MergeSort", mergesort_topdown, trabajo)
  elif opcion == "q":
    ejecutar_y_medir_rango("QuickSort", quicksort, trabajo)
  elif opcion == "h":
    ejecutar_y_medir("HeapSort", heapsort, trabajo)
  else:
    print("Opcion no reconocida.")
    return

  print("Despues:", trabajo[:20], "...")

if __name__ == "__main__":
  menu()