# archivo: ordenamientos.py
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

datos = [29, 10, 14, 37, 13, 5, 88, 1]
quicksort(datos, 0, len(datos) - 1)
print(datos)