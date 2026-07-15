class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock
        self.izquierdo = None
        self.derecho = None


class ArbolInventario:
    def __init__(self):
        self.raiz = None

    def crear_producto(self, codigo, stock):
        return Producto(codigo, stock)

    def insertar(self, nodo, codigo, stock):
        if nodo is None:
            return self.crear_producto(codigo, stock)
        if codigo == nodo.codigo:
            nodo.stock += stock
        elif codigo < nodo.codigo:
            nodo.izquierdo = self.insertar(nodo.izquierdo, codigo, stock)
        else:
            nodo.derecho = self.insertar(nodo.derecho, codigo, stock)
        return nodo

    def insertar_producto(self, codigo, stock):
        self.raiz = self.insertar(self.raiz, codigo, stock)
        return self.raiz

    def buscar(self, nodo, codigo):
        if nodo is None:
            return None
        if codigo == nodo.codigo:
            return nodo
        if codigo < nodo.codigo:
            return self.buscar(nodo.izquierdo, codigo)
        return self.buscar(nodo.derecho, codigo)

    def imprimir_inorden(self, nodo):
        if nodo is None:
            return
        self.imprimir_inorden(nodo.izquierdo)
        print(f"Codigo {nodo.codigo}: {nodo.stock} unidades")
        self.imprimir_inorden(nodo.derecho)


if __name__ == "__main__":
    inventario = ArbolInventario()
    inventario.insertar_producto(1050, 12)
    inventario.insertar_producto(900, 6)
    inventario.insertar_producto(1400, 5)
    inventario.insertar_producto(850, 20)
    inventario.insertar_producto(1100, 8)
    inventario.insertar_producto(1600, 3)
    inventario.insertar_producto(900, 4)  # reingreso

    print("Inventario ordenado:")
    inventario.imprimir_inorden(inventario.raiz)

    codigo_consulta = 1100
    encontrado = inventario.buscar(inventario.raiz, codigo_consulta)
    if encontrado:
        print(f"\nStock del producto {codigo_consulta}: {encontrado.stock} unidades")
    else:
        print(f"\nEl producto {codigo_consulta} no existe")