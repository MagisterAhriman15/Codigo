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

datos = [5, 2, 9, 1, 3]
print("Antes: ", end="")
imprimir_lista(datos)
print()

bubble_sort(datos)

print("Despues: ", end="")
imprimir_lista(datos)
print()