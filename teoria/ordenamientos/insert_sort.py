def imprimir_lista(valores):
  for valor in valores:
    print(valor, end=", ")

def insertion_sort(valores):
  for i in range(1, len(valores)):
    actual = valores[i]
    j = i - 1
    while j >= 0 and valores[j] > actual:
      valores[j + 1] = valores[j]
      j -= 1
    valores[j + 1] = actual

datos = [7, 4, 5, 2, 9]
print("Antes: ", end="")
imprimir_lista(datos)
print()

insertion_sort(datos)

print("Despues: ", end="")
imprimir_lista(datos)
print()