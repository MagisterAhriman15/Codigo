def validar_parentesis(texto):
  pila = []
  pares = {')': '(', ']': '[', '}': '{'}

  for c in texto:
    if c in '([{':
      pila.append(c)
    elif c in ')]}':
      if not pila or pila.pop() != pares[c]:
        return False

  return len(pila) == 0


if __name__ == "__main__":
  casos = [
    "(a + b) * (c + d)",
    "([{}])",
    "( [ ) ]",
    "funcion(x[2] + arr{1})",
  ]

  for texto in casos:
    print(texto, "=>", "OK" if validar_parentesis(texto) else "ERROR")