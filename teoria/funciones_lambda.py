def operar(v1,v2,fn):
    return fn(v1,v2)

resu1=operar(10,3,lambda x1,x2: x1+x2)
print(resu1)

resu2=operar(10,3,lambda x1,x2: x1-x2)
print(resu2)

print(operar(30,10,lambda x1,x2: x1*x2))

print(operar(10,2,lambda x1,x2: x1/x2))