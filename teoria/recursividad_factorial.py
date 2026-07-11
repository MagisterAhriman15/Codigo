def factorial(fact):
    if fact>0:
        valor=fact*factorial(fact-1)
        return valor
    else:
        return 1;

print(f"El factorial de 4 es {factorial(4)}")