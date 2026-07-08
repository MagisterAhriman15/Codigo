import random
import os

def lanzar_pool_dados(cantidad_dados):
    resultados = []
    
    # Usamos '_' en el for cuando no nos importa el índice, solo repetir la acción
    for _ in range(cantidad_dados):
        # Simulamos un dado de 20 caras
        tirada = random.randint(1, 20)
        resultados.append(tirada)
        
    return resultados
    
def limpiar_consola():
    # 'nt' corresponde a Windows
    if os.name == 'nt':
        os.system('cls')
    # Para macOS y Linux (posix)
    else:
        os.system('clear')
    
flag=True

while(flag):
    limpiar_consola()
    print("Bienvenido al lanzador de dados")
    print("Ingresar números naturales, si desea cerrar el programa ingresar 0 como cantidad de dados")
    cantidad_dados_str = input("¿Cuántos dados deseas lanzar? ")
    
    try:
        cantidad_dados = int(cantidad_dados_str)
    except ValueError:
        print("¡Error! Has introducido letras o caracteres inválidos. Debes escribir un número entero.")
        input("Presiona Enter para volver a intentarlo...")
        continue
    
    if cantidad_dados<0:
        print("Has ingresado un número negativo, ingresar un valor positivo")
        input("Presiona Enter para volver a intentarlo...")
        continue
    elif cantidad_dados==0:
        input("Presiona Enter para finalizar el programa...")
        break
    else:
        dados = lanzar_pool_dados(cantidad_dados)
        print(f"Resultados de la tirada: {dados}")
    
    input("Presiona Enter para volver a ejecutar el programa...")