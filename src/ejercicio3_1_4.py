"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""

def numeros_ganadores():
    numeros = []
    
    for i in range(6):
        numeroganador= int(input("Introduce los nºs ganadores de la lotería: "))
        numeros.append(numeroganador)
    print(numeros.sort())

    for numeroganador in numeros:
        print(numeroganador)

numeros_ganadores()
