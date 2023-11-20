"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70"""

def precio_frutas():
    fruteria = {"Plátano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

    fruta = input("Fruta a desear: ").title()
    kilos = float(input("¿Cuantos kilos se lleva? "))

    if fruta in fruteria:
        print(round((fruteria[fruta]*kilos),2))

    else:
        print("Lo siento no está en la lista.")

precio_frutas()