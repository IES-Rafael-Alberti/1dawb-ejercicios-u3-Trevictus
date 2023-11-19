"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante."""

def letras():
    letras = list(map(chr, range(97, 123)))
    lista = []
    
    for i, letra in enumerate(letras, start = 1):
        if i % 3 !=0:
            lista.append(letra)

    print(lista)

letras()