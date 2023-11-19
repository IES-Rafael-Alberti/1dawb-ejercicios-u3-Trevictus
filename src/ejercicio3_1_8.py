"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

def pedir_palabra():
    palabra = str(input("Introduce una palabra: "))

    if palabra == palabra[::-1]:
        print("Es un palíndromo.")

    else:
        print("No es un palíndromo.")


pedir_palabra()