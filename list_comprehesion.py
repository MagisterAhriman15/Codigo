correos=["ana@gmail.com","", None, "carlos@yahoo.com"]
correctos=[]
for correo in correos:
    if correo:
        correctos.append(correo)
print(correctos)

emails=["ana@gmail.com", "", None,"carlos@yahoo.com"]
validos=[e for e in emails if e]
print(validos)

numeros=[1, 2, 3, 4]
cuadrados=[n**2 for n in numeros]
print(cuadrados)