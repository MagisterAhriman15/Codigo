class Jugador:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        self.izquierdo = None
        self.derecho = None


class ArbolRanking:
    def __init__(self):
        self.raiz = None

    def crear_jugador(self, nombre, puntaje):
        return Jugador(nombre, puntaje)

    def insertar(self, nodo, nombre, puntaje):
        if nodo is None:
            return self.crear_jugador(nombre, puntaje)
        if puntaje < nodo.puntaje:
            nodo.izquierdo = self.insertar(nodo.izquierdo, nombre, puntaje)
        else:
            nodo.derecho = self.insertar(nodo.derecho, nombre, puntaje)
        return nodo

    def insertar_jugador(self, nombre, puntaje):
        self.raiz = self.insertar(self.raiz, nombre, puntaje)
        return self.raiz

    def buscar_por_puntaje(self, nodo, puntaje):
        if nodo is None:
            return None
        if puntaje == nodo.puntaje:
            return nodo
        if puntaje < nodo.puntaje:
            return self.buscar_por_puntaje(nodo.izquierdo, puntaje)
        return self.buscar_por_puntaje(nodo.derecho, puntaje)

    def imprimir_tabla_desc(self, nodo):
        if nodo is None:
            return
        self.imprimir_tabla_desc(nodo.derecho)
        print(f"{nodo.nombre} - {nodo.puntaje}")
        self.imprimir_tabla_desc(nodo.izquierdo)


if __name__ == "__main__":
    ranking = ArbolRanking()
    ranking.insertar_jugador("Ana", 1800)
    ranking.insertar_jugador("Bruno", 1650)
    ranking.insertar_jugador("Carla", 2050)
    ranking.insertar_jugador("Diego", 1500)
    ranking.insertar_jugador("Elena", 1900)
    ranking.insertar_jugador("Facundo", 2100)
    ranking.insertar_jugador("Gael", 1900)  # puntaje repetido

    print("Tabla descendente:")
    ranking.imprimir_tabla_desc(ranking.raiz)

    consulta = 1900
    jugador = ranking.buscar_por_puntaje(ranking.raiz, consulta)
    if jugador:
        print(f"\\nPrimer jugador con {consulta} puntos: {jugador.nombre}")
    else:
        print(f"\\nNo hay jugadores con {consulta} puntos")