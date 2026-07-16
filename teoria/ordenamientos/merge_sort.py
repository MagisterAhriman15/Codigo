# archivo: ordenamientos.py
def merge(valores, inicio, medio, fin):
  buffer = []
  i = inicio
  j = medio + 1
  while i <= medio and j <= fin:
    if valores[i] <= valores[j]:
      buffer.append(valores[i])
      i += 1
    else:
      buffer.append(valores[j])
      j += 1
  while i <= medio:
    buffer.append(valores[i])
    i += 1
  while j <= fin:
    buffer.append(valores[j])
    j += 1
  valores[inicio:fin + 1] = buffer

def mergesort(valores, inicio, fin):
  if inicio >= fin:
    return
  medio = (inicio + fin) // 2
  mergesort(valores, inicio, medio)
  mergesort(valores, medio + 1, fin)
  merge(valores, inicio, medio, fin)

datos = [42, 7, 18, 3, 25]
mergesort(datos, 0, len(datos) - 1)
print(datos)