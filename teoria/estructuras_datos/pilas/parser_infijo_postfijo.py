PRECEDENCIA = {'+': 1, '-': 1, '*': 2, '/': 2}


def es_operador(tok):
  return tok in PRECEDENCIA


def infijo_a_postfijo(expr):
  salida = []
  ops = []
  tokens = expr.split()

  for tok in tokens:
    if tok.isdigit():
      salida.append(tok)
    elif tok == '(':
      ops.append(tok)
    elif tok == ')':
      while ops and ops[-1] != '(':
        salida.append(ops.pop())
      ops.pop()
    elif es_operador(tok):
      while ops and ops[-1] != '(' and PRECEDENCIA.get(ops[-1], 0) >= PRECEDENCIA[tok]:
        salida.append(ops.pop())
      ops.append(tok)

  while ops:
    salida.append(ops.pop())
  return salida


def evaluar_postfija(tokens):
  pila = []
  for tok in tokens:
    if tok.isdigit():
      pila.append(float(tok))
    else:
      b = pila.pop()
      a = pila.pop()
      if tok == '+':
        pila.append(a + b)
      elif tok == '-':
        pila.append(a - b)
      elif tok == '*':
        pila.append(a * b)
      elif tok == '/':
        pila.append(a / b)
  return pila.pop()


if __name__ == "__main__":
  expr = "3 + 4 * 2 / ( 1 - 5 )"
  postfija = infijo_a_postfijo(expr)
  print("Postfija:", " ".join(postfija))
  print("Resultado:", round(evaluar_postfija(postfija), 2))