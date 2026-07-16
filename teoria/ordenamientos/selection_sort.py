def swap(valores, i, j):
  valores[i], valores[j] = valores[j], valores[i]

def imprimir_lista(valores):
  for valor in valores:
    print(valor, end=", ")

def selection_sort(valores):
  for i in range(len(valores) - 1):
    indice_min = i
    for j in range(i + 1, len(valores)):
      if valores[j] < valores[indice_min]:
        indice_min = j
    if indice_min != i:
      swap(valores, i, indice_min)

datos = [6, 1, 8, 3, 4]
print("Antes: ", end="")
imprimir_lista(datos)
print()

selection_sort(datos)

print("Despues: ", end="")
imprimir_lista(datos)
print()