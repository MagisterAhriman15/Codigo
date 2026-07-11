def operar(v1,v2,fn):
    return fn(v1,v2)

def sumar(x1,x2):
    return x1+x2

def restar(x1,x2):
    return x1-x2

def multiplicar(x1,x2):
    return x1*x2

def dividir(x1,x2):
    return x1/x2

resu1=operar(10,3,sumar)
print(resu1)

resu2=operar(10,3,restar)
print(resu2)

print(operar(30,10,multiplicar))

print(operar(10,2,dividir))