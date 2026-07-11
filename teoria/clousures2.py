def crear_contador(inicio=0):
    contador = inicio  # variable libre que la función interna "recuerda"
    
    def incrementar():
        nonlocal contador  # para modificar la variable del closure
        contador += 1
        return contador
    
    return incrementar


# Crear dos contadores independientes
contador_a = crear_contador(10)
contador_b = crear_contador(100)

print(contador_a())  # 11
print(contador_a())  # 12
print(contador_b())  # 101
print(contador_a())  # 13
print(contador_b())  # 102