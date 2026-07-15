import random


class Nodo:
  def __init__(self, etiqueta, palabra=None, es_hoja=False, es_alternativa=False):
    self.etiqueta = etiqueta
    self.palabra = palabra or ""
    self.es_hoja = es_hoja
    self.es_alternativa = es_alternativa
    self.primer_hijo = None
    self.siguiente_hermano = None


def agregar_hijo(padre, hijo):
  if padre is None or hijo is None:
    return
  if padre.primer_hijo is None:
    padre.primer_hijo = hijo
    return
  actual = padre.primer_hijo
  while actual.siguiente_hermano:
    actual = actual.siguiente_hermano
  actual.siguiente_hermano = hijo


def contar_hijos(nodo):
  total = 0
  hijo = nodo.primer_hijo if nodo else None
  while hijo:
    total += 1
    hijo = hijo.siguiente_hermano
  return total


def hijo_aleatorio(nodo):
  total = contar_hijos(nodo)
  if total == 0:
    return None
  indice = random.randrange(total)
  actual = nodo.primer_hijo
  while indice > 0 and actual:
    actual = actual.siguiente_hermano
    indice -= 1
  return actual


def generar_frase(nodo, tokens):
  if nodo is None:
    return
  if nodo.es_hoja:
    tokens.append(nodo.palabra)
    return
  if nodo.es_alternativa:
    seleccion = hijo_aleatorio(nodo)
    if seleccion:
      generar_frase(seleccion, tokens)
    return
  actual = nodo.primer_hijo
  while actual:
    generar_frase(actual, tokens)
    actual = actual.siguiente_hermano


def mostrar_mapa(nodo, nivel=0):
  if nodo is None:
    return
  marca = " (alt)" if nodo.es_alternativa else ""
  print("  " * nivel + f"- {nodo.etiqueta}{marca}")
  if nodo.es_hoja:
    print("  " * (nivel + 1) + f"` {nodo.palabra}")
  hijo = nodo.primer_hijo
  while hijo:
    mostrar_mapa(hijo, nivel + 1)
    hijo = hijo.siguiente_hermano


def crear_gramatica():
  oracion = Nodo("Oracion")
  sujeto = Nodo("Sujeto")
  predicado = Nodo("Predicado")
  agregar_hijo(oracion, sujeto)
  agregar_hijo(oracion, predicado)

  articulo = Nodo("Articulo", es_alternativa=True)
  sustantivo = Nodo("Sustantivo", es_alternativa=True)
  agregar_hijo(sujeto, articulo)
  agregar_hijo(sujeto, sustantivo)

  verbo = Nodo("Verbo", es_alternativa=True)
  complemento = Nodo("Complemento", es_alternativa=True)
  agregar_hijo(predicado, verbo)
  agregar_hijo(predicado, complemento)

  agregar_hijo(articulo, Nodo("Articulo", "el", es_hoja=True))
  agregar_hijo(articulo, Nodo("Articulo", "la", es_hoja=True))
  agregar_hijo(articulo, Nodo("Articulo", "un", es_hoja=True))

  agregar_hijo(sustantivo, Nodo("Sustantivo", "intérprete", es_hoja=True))
  agregar_hijo(sustantivo, Nodo("Sustantivo", "compilador", es_hoja=True))
  agregar_hijo(sustantivo, Nodo("Sustantivo", "framework", es_hoja=True))

  agregar_hijo(verbo, Nodo("Verbo", "configura", es_hoja=True))
  agregar_hijo(verbo, Nodo("Verbo", "ejecuta", es_hoja=True))
  agregar_hijo(verbo, Nodo("Verbo", "optimiza", es_hoja=True))

  comp_nominal = Nodo("ComplementoNominal")
  comp_prepo = Nodo("ComplementoPreposicional")
  agregar_hijo(complemento, comp_nominal)
  agregar_hijo(complemento, comp_prepo)

  art_nom = Nodo("Articulo", es_alternativa=True)
  sus_nom = Nodo("Sustantivo", es_alternativa=True)
  agregar_hijo(comp_nominal, art_nom)
  agregar_hijo(comp_nominal, sus_nom)
  agregar_hijo(art_nom, Nodo("Articulo", "el", es_hoja=True))
  agregar_hijo(art_nom, Nodo("Articulo", "su", es_hoja=True))
  agregar_hijo(sus_nom, Nodo("Sustantivo", "analizador", es_hoja=True))
  agregar_hijo(sus_nom, Nodo("Sustantivo", "módulo", es_hoja=True))
  agregar_hijo(sus_nom, Nodo("Sustantivo", "pipeline", es_hoja=True))

  prep_comp = Nodo("Preposicion", es_alternativa=True)
  sus_comp = Nodo("Sustantivo", es_alternativa=True)
  agregar_hijo(comp_prepo, prep_comp)
  agregar_hijo(comp_prepo, sus_comp)
  agregar_hijo(prep_comp, Nodo("Preposicion", "sobre microservicios", es_hoja=True))
  agregar_hijo(prep_comp, Nodo("Preposicion", "para despliegues", es_hoja=True))
  agregar_hijo(prep_comp, Nodo("Preposicion", "con monitoreo", es_hoja=True))
  agregar_hijo(sus_comp, Nodo("Sustantivo", "orquestador", es_hoja=True))
  agregar_hijo(sus_comp, Nodo("Sustantivo", "servicio", es_hoja=True))
  agregar_hijo(sus_comp, Nodo("Sustantivo", "cluster", es_hoja=True))

  return oracion


if __name__ == "__main__":
  random.seed()
  gramatica = crear_gramatica()

  print("=== Frases generadas ===")
  for i in range(5):
    tokens = []
    generar_frase(gramatica, tokens)
    frase = " ".join(tokens).strip()
    print(f"{i + 1}) {frase}.")

  print("\n=== Vista del árbol ===")
  mostrar_mapa(gramatica)