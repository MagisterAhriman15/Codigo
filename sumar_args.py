def sumar(*args):
    total=0
    for numero in args:
        total+=numero
    return total

resultado=sumar(3, 5, 7, 10)
print(resultado)