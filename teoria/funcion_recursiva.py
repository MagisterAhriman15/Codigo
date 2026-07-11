"""def imprimir(x):
    print(x)
    imprimir(x-1)

imprimir(5)"""
#Se bloquea por ser un loop infinito

def imprimir(x):
    if x>0:
        print(x)
        imprimir(x-1)

imprimir(100)