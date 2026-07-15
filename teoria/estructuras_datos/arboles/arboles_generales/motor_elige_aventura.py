class Opcion:
  def __init__(self, texto, destino):
    self.texto = texto
    self.destino = destino


class Nodo:
  def __init__(self, descripcion):
    self.descripcion = descripcion
    self.opciones = []


def crear_nodo(descripcion):
  return Nodo(descripcion)


def agregar_opcion(nodo, texto, destino):
  if nodo is None or destino is None:
    return
  nodo.opciones.append(Opcion(texto, destino))


def crear_historia():
  inicio = crear_nodo("Al amanecer despiertas junto al camino principal. "
                      "El bosque murmura y una columna de humo se alza a lo lejos.")
  rio = crear_nodo("Sigues el rumor del rio y encuentras un puente de madera.")
  colina = crear_nodo("Subes la colina y descubres una fogata reciente.")
  bosque = crear_nodo("Te internas en el bosque y tres sendas se cruzan en un claro.")
  aldea = crear_nodo("Llegas a una aldea silenciosa; las puertas estan abiertas.")
  cueva = crear_nodo("Encuentras una cueva iluminada por cristales azules.")
  laguna = crear_nodo("Ante ti hay una laguna cristalina con un muelle oculto.")
  torre = crear_nodo("La torre de vigilancia cruje mientras el viento la azota.")
  campamento = crear_nodo("Un campamento vacio guarda restos de provisiones.")
  mercado = crear_nodo("Sigues a un zorro y descubres un mercado ambulante.")

  final_rio = crear_nodo("El pescador comparte comida y canciones. Descansas feliz.")
  final_colina = crear_nodo("Avivas la fogata y pasas la noche bajo las estrellas. Fin.")
  final_aldea = crear_nodo("Ayudas a reparar las defensas de la aldea. Te conviertes en su guardian.")
  final_desierto = crear_nodo("Marchas al desierto y nuevas aventuras te esperan lejos.")
  final_bosque = crear_nodo("El arbol hueco canta historias y te duermes en el claro.")
  final_laguna = crear_nodo("Nadas hasta el muelle y hallas un cuaderno olvidado. Fin.")
  final_agua = crear_nodo("Guardas agua brillante y sigues tu viaje reconfortado.")
  final_mercado = crear_nodo("Degustas especias extrañas y compartes risas con mercaderes.")
  final_brujula = crear_nodo("Obtienes una brujula que apunta a nuevas rutas legendarias.")
  final_campamento = crear_nodo("Descansas en una hamaca improvisada hasta el atardecer.")
  final_provisiones = crear_nodo("Empacas provisiones frescas y retomas la marcha con energía.")
  final_cueva = crear_nodo("Conversas con una criatura subterranea y recibes consejos.")
  final_cristal = crear_nodo("Los cristales te guian a un corredor iluminado que te devuelve al camino.")
  final_torre = crear_nodo("Enciendes la alarma y adviertes a viajeros lejanos. Eres un heroe.")
  final_horizonte = crear_nodo("Desde la torre observas el amanecer y trazas nuevos planes.")

  agregar_opcion(inicio, "Tomar el sendero del rio", rio)
  agregar_opcion(inicio, "Subir la colina humeante", colina)
  agregar_opcion(inicio, "Explorar el bosque espeso", bosque)

  agregar_opcion(rio, "Cruzar el puente hacia la aldea", aldea)
  agregar_opcion(rio, "Descender al cauce y explorar cuevas", cueva)
  agregar_opcion(rio, "Descansar a la orilla para pescar", final_rio)

  agregar_opcion(colina, "Avivar la fogata y esperar", final_colina)
  agregar_opcion(colina, "Subir a la torre de vigilancia", torre)
  agregar_opcion(colina, "Bajar por un sendero hacia el valle", campamento)

  agregar_opcion(bosque, "Seguir las luciernagas hasta una laguna", laguna)
  agregar_opcion(bosque, "Escuchar al arbol hueco", final_bosque)
  agregar_opcion(bosque, "Perseguir al zorro hasta un mercado", mercado)

  agregar_opcion(aldea, "Ofrecer ayuda a los habitantes", final_aldea)
  agregar_opcion(aldea, "Seguir camino hacia el desierto", final_desierto)

  agregar_opcion(cueva, "Hablar con el eco subterraneo", final_cueva)
  agregar_opcion(cueva, "Seguir un tunel iluminado", final_cristal)

  agregar_opcion(laguna, "Nadar hasta el muelle oculto", final_laguna)
  agregar_opcion(laguna, "Recolectar agua brillante y partir", final_agua)

  agregar_opcion(torre, "Encender la alarma de emergencia", final_torre)
  agregar_opcion(torre, "Observar el horizonte en silencio", final_horizonte)

  agregar_opcion(campamento, "Descansar entre las tiendas", final_campamento)
  agregar_opcion(campamento, "Tomar provisiones y volver al camino", final_provisiones)

  agregar_opcion(mercado, "Comer en un puesto de especias", final_mercado)
  agregar_opcion(mercado, "Comprar una brujula misteriosa", final_brujula)

  return inicio


def jugar(inicio):
  if inicio is None:
    return
  actual = inicio

  while actual:
    print("\n---------------------------")
    print(actual.descripcion)
    if not actual.opciones:
      print("\nFin de la historia. Gracias por jugar.")
      break

    for indice, opcion in enumerate(actual.opciones, start=1):
      print(f"{indice}) {opcion.texto}")
    eleccion = input("Selecciona una opcion: ").strip()
    if not eleccion.isdigit():
      print("Opcion invalida, intenta nuevamente.")
      continue
    indice = int(eleccion)
    if indice < 1 or indice > len(actual.opciones):
      print("Opcion invalida, intenta nuevamente.")
      continue
    actual = actual.opciones[indice - 1].destino


def mostrar_mapa(nodo, nivel=0):
  if nodo is None:
    return
  print("  " * nivel + f"* {nodo.descripcion}")
  for indice, opcion in enumerate(nodo.opciones, start=1):
    print("  " * (nivel + 1) + f"({indice}) {opcion.texto}")
    mostrar_mapa(opcion.destino, nivel + 2)


if __name__ == "__main__":
  aventura = crear_historia()
  jugar(aventura)
  print("\n=== Mapa completo de escenas ===")
  mostrar_mapa(aventura)