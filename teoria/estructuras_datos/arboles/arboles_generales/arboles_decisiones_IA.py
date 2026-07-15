class TipoDecision:
  COLOR = "color"
  TAMANO = "tamano"
  TEXTURA = "textura"
  OLOR = "olor"
  SABOR = "sabor"
  CLASIFICACION = "clasificacion"


class Opcion:
  def __init__(self, valor, etiqueta, destino):
    self.valor = valor
    self.etiqueta = etiqueta
    self.destino = destino


class DecisionNode:
  def __init__(self, tipo, pregunta=None, clasificacion=None):
    self.tipo = tipo
    self.pregunta = pregunta or ""
    self.clasificacion = clasificacion or ""
    self.opciones = []


class Color:
  ROJO = 0
  AMARILLO = 1
  VERDE = 2


class Tamano:
  PEQUENO = 0
  MEDIANO = 1
  GRANDE = 2


class Textura:
  LISA = 0
  RUGOSA = 1


class Olor:
  NEUTRO = 0
  FRAGANTE = 1


class Sabor:
  DULCE = 0
  ACIDO = 1


class Objeto:
  def __init__(self, color, tamano, textura, olor, sabor):
    self.color = color
    self.tamano = tamano
    self.textura = textura
    self.olor = olor
    self.sabor = sabor


def crear_nodo_pregunta(tipo, pregunta):
  return DecisionNode(tipo, pregunta=pregunta)


def crear_nodo_clasificacion(nombre):
  return DecisionNode(TipoDecision.CLASIFICACION, clasificacion=nombre)


def agregar_opcion(padre, valor, etiqueta, destino):
  if padre is None or destino is None:
    return
  padre.opciones.append(Opcion(valor, etiqueta, destino))


def valor_atributo(obj, tipo):
  if tipo == TipoDecision.COLOR:
    return obj.color
  if tipo == TipoDecision.TAMANO:
    return obj.tamano
  if tipo == TipoDecision.TEXTURA:
    return obj.textura
  if tipo == TipoDecision.OLOR:
    return obj.olor
  if tipo == TipoDecision.SABOR:
    return obj.sabor
  return None


def clasificar(nodo, obj):
  if nodo is None or obj is None:
    return "Desconocido"
  if nodo.tipo == TipoDecision.CLASIFICACION:
    return nodo.clasificacion
  valor = valor_atributo(obj, nodo.tipo)
  for opcion in nodo.opciones:
    if opcion.valor == valor:
      return clasificar(opcion.destino, obj)
  return "Desconocido"


def clasificar_interactivo(nodo):
  if nodo is None:
    return "Desconocido"
  actual = nodo
  while actual and actual.tipo != TipoDecision.CLASIFICACION:
    print(f"\n{actual.pregunta}")
    for indice, opcion in enumerate(actual.opciones, start=1):
      print(f"  {indice}) {opcion.etiqueta}")
    entrada = input("Selecciona una opcion: ").strip()
    if not entrada.isdigit():
      print("Opcion invalida, intenta de nuevo.")
      continue
    seleccion = int(entrada)
    if seleccion <= 0 or seleccion > len(actual.opciones):
      print("Seleccion fuera de rango.")
      continue
    actual = actual.opciones[seleccion - 1].destino
  return actual.clasificacion if actual else "Desconocido"


def crear_arbol_frutas():
  raiz = crear_nodo_pregunta(TipoDecision.COLOR, "Color?")

  n_rojo = crear_nodo_pregunta(TipoDecision.TAMANO, "Tamanio?")
  n_amarillo = crear_nodo_pregunta(TipoDecision.TEXTURA, "Textura?")
  n_verde = crear_nodo_pregunta(TipoDecision.SABOR, "Sabor?")
  agregar_opcion(raiz, Color.ROJO, "Rojo", n_rojo)
  agregar_opcion(raiz, Color.AMARILLO, "Amarillo", n_amarillo)
  agregar_opcion(raiz, Color.VERDE, "Verde", n_verde)

  rojo_grande = crear_nodo_pregunta(TipoDecision.TEXTURA, "Textura?")
  rojo_mediano = crear_nodo_pregunta(TipoDecision.OLOR, "Olor?")
  rojo_pequeno = crear_nodo_pregunta(TipoDecision.SABOR, "Sabor?")
  agregar_opcion(n_rojo, Tamano.GRANDE, "Grande", rojo_grande)
  agregar_opcion(n_rojo, Tamano.MEDIANO, "Mediano", rojo_mediano)
  agregar_opcion(n_rojo, Tamano.PEQUENO, "Pequeno", rojo_pequeno)

  agregar_opcion(rojo_grande, Textura.LISA, "Lisa", crear_nodo_clasificacion("Manzana Crimson"))
  rojo_grande_rugosa = crear_nodo_pregunta(TipoDecision.SABOR, "Sabor?")
  agregar_opcion(rojo_grande, Textura.RUGOSA, "Rugosa", rojo_grande_rugosa)
  agregar_opcion(rojo_grande_rugosa, Sabor.DULCE, "Dulce", crear_nodo_clasificacion("Granada dulce"))
  agregar_opcion(rojo_grande_rugosa, Sabor.ACIDO, "Acido", crear_nodo_clasificacion("Pomelo rosado"))

  agregar_opcion(rojo_mediano, Olor.FRAGANTE, "Fragante", crear_nodo_clasificacion("Frutilla fragante"))
  rojo_mediano_neutro = crear_nodo_pregunta(TipoDecision.SABOR, "Sabor?")
  agregar_opcion(rojo_mediano, Olor.NEUTRO, "Neutro", rojo_mediano_neutro)
  agregar_opcion(rojo_mediano_neutro, Sabor.DULCE, "Dulce", crear_nodo_clasificacion("Ciruela roja"))
  agregar_opcion(rojo_mediano_neutro, Sabor.ACIDO, "Acido", crear_nodo_clasificacion("Arandano rojo"))

  rojo_pequeno_textura = crear_nodo_pregunta(TipoDecision.TEXTURA, "Textura?")
  agregar_opcion(rojo_pequeno, Sabor.DULCE, "Dulce", rojo_pequeno_textura)
  agregar_opcion(rojo_pequeno, Sabor.ACIDO, "Acido", crear_nodo_clasificacion("Grosella roja"))
  agregar_opcion(rojo_pequeno_textura, Textura.LISA, "Lisa", crear_nodo_clasificacion("Cereza"))
  agregar_opcion(rojo_pequeno_textura, Textura.RUGOSA, "Rugosa", crear_nodo_clasificacion("Frambuesa"))

  amarillo_lisa = crear_nodo_pregunta(TipoDecision.TAMANO, "Tamanio?")
  amarillo_rugosa = crear_nodo_pregunta(TipoDecision.SABOR, "Sabor?")
  agregar_opcion(n_amarillo, Textura.LISA, "Lisa", amarillo_lisa)
  agregar_opcion(n_amarillo, Textura.RUGOSA, "Rugosa", amarillo_rugosa)
  agregar_opcion(amarillo_lisa, Tamano.GRANDE, "Grande", crear_nodo_clasificacion("Papaya dorada"))
  agregar_opcion(amarillo_lisa, Tamano.MEDIANO, "Mediano", crear_nodo_clasificacion("Mango ataulfo"))
  agregar_opcion(amarillo_lisa, Tamano.PEQUENO, "Pequeno", crear_nodo_clasificacion("Banana baby"))
  agregar_opcion(amarillo_rugosa, Sabor.DULCE, "Dulce", crear_nodo_clasificacion("Maracuya amarilla"))
  agregar_opcion(amarillo_rugosa, Sabor.ACIDO, "Acido", crear_nodo_clasificacion("Limon rugoso"))

  verde_acido = crear_nodo_pregunta(TipoDecision.TAMANO, "Tamanio?")
  verde_dulce = crear_nodo_pregunta(TipoDecision.TEXTURA, "Textura?")
  agregar_opcion(n_verde, Sabor.ACIDO, "Acido", verde_acido)
  agregar_opcion(n_verde, Sabor.DULCE, "Dulce", verde_dulce)
  agregar_opcion(verde_acido, Tamano.PEQUENO, "Pequeno", crear_nodo_clasificacion("Lima"))
  verde_acido_grande = crear_nodo_pregunta(TipoDecision.TEXTURA, "Textura?")
  agregar_opcion(verde_acido, Tamano.GRANDE, "Grande", verde_acido_grande)
  agregar_opcion(verde_acido_grande, Textura.LISA, "Lisa", crear_nodo_clasificacion("Manzana verde"))
  agregar_opcion(verde_acido_grande, Textura.RUGOSA, "Rugosa", crear_nodo_clasificacion("Pomelo verde"))
  agregar_opcion(verde_dulce, Textura.LISA, "Lisa", crear_nodo_clasificacion("Uva verde"))
  verde_dulce_rugosa = crear_nodo_pregunta(TipoDecision.TAMANO, "Tamanio?")
  agregar_opcion(verde_dulce, Textura.RUGOSA, "Rugosa", verde_dulce_rugosa)
  agregar_opcion(verde_dulce_rugosa, Tamano.PEQUENO, "Pequeno", crear_nodo_clasificacion("Kiwi"))
  agregar_opcion(verde_dulce_rugosa, Tamano.MEDIANO, "Mediano", crear_nodo_clasificacion("Melon verde"))

  return raiz


if __name__ == "__main__":
  raiz = crear_arbol_frutas()

  muestras = [
    Objeto(Color.ROJO, Tamano.GRANDE, Textura.LISA, Olor.NEUTRO, Sabor.DULCE),
    Objeto(Color.ROJO, Tamano.PEQUENO, Textura.RUGOSA, Olor.NEUTRO, Sabor.DULCE),
    Objeto(Color.AMARILLO, Tamano.MEDIANO, Textura.LISA, Olor.NEUTRO, Sabor.DULCE),
    Objeto(Color.AMARILLO, Tamano.PEQUENO, Textura.RUGOSA, Olor.NEUTRO, Sabor.ACIDO),
    Objeto(Color.VERDE, Tamano.PEQUENO, Textura.RUGOSA, Olor.NEUTRO, Sabor.DULCE),
    Objeto(Color.VERDE, Tamano.GRANDE, Textura.LISA, Olor.NEUTRO, Sabor.ACIDO)
  ]

  nombres = ["Caso A", "Caso B", "Caso C", "Caso D", "Caso E", "Caso F"]
  print("=== Clasificacion automatica ===")
  for nombre, muestra in zip(nombres, muestras):
    print(f"{nombre} => {clasificar(raiz, muestra)}")

  print("\n=== Sesion interactiva ===")
  resultado = clasificar_interactivo(raiz)
  print(f"Resultado: {resultado}")