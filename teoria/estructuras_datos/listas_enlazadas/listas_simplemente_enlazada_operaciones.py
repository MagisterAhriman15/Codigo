class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class Lista:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        reco = self.cabeza
        while reco.sig:
            reco = reco.sig
        reco.sig = nuevo

    def insertar_en(self, posicion, valor):
        if posicion <= 0 or self.cabeza is None:
            return self.insertar_inicio(valor)
        reco = self.cabeza
        for _ in range(posicion - 1):
            if reco is None:
                return
            reco = reco.sig
        if reco is None:
            return
        nuevo = Nodo(valor)
        nuevo.sig = reco.sig
        reco.sig = nuevo

    def eliminar_primero(self):
        if self.cabeza is None:
            return None
        victima = self.cabeza
        self.cabeza = victima.sig
        victima.sig = None
        return victima.valor

    def eliminar_ultimo(self):
        if self.cabeza is None:
            return None
        if self.cabeza.sig is None:
            valor = self.cabeza.valor
            self.cabeza = None
            return valor
        reco = self.cabeza
        while reco.sig and reco.sig.sig:
            reco = reco.sig
        valor = reco.sig.valor
        reco.sig = None
        return valor

    def eliminar_valor(self, valor):
        if self.cabeza is None:
            return False
        if self.cabeza.valor == valor:
            self.eliminar_primero()
            return True
        reco = self.cabeza
        while reco.sig and reco.sig.valor != valor:
            reco = reco.sig
        if reco.sig is None:
            return False
        victima = reco.sig
        reco.sig = victima.sig
        victima.sig = None
        return True

    def buscar(self, valor):
        reco = self.cabeza
        while reco:
            if reco.valor == valor:
                return reco
            reco = reco.sig
        return None

    def imprimir(self):
        reco = self.cabeza
        while reco:
            print(reco.valor, end=" -> ")
            reco = reco.sig
        print("None")

    def limpiar(self):
        while self.cabeza:
            siguiente = self.cabeza.sig
            self.cabeza.sig = None
            self.cabeza = siguiente


def main():
    lista = Lista()
    lista.insertar_inicio(10)
    lista.insertar_final(20)
    lista.insertar_en(1, 15)
    print("Lista despues de insertar 10, 20 y 15 en el medio:")
    lista.imprimir()
    lista.eliminar_valor(15)
    lista.eliminar_ultimo()
    print("Lista despues de eliminar 15 y el ultimo:")
    lista.imprimir()
    lista.limpiar()


if __name__ == "__main__":
    main()