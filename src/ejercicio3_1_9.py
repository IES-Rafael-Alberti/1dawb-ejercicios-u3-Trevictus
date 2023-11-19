"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""

def pedir_palabra():
    palabra = input("Introduce una palabra: ")
    vocales = ["a", "e", "i", "o", "u"]

    for vocal in vocales:
        cantidad = palabra.count(vocal)

        print("La vocal", vocal, "aparece", cantidad, "veces en la palabra", palabra)

pedir_palabra()