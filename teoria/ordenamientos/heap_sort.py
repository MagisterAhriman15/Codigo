# archivo: ordenamientos.py
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

datos = [16, 7, 3, 20, 17, 8, 10, 1]
heapsort(datos)
print(datos)