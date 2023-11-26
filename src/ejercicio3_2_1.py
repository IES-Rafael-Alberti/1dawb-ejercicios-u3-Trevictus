"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""


def divisas():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = input("¿Cuál es la divisa a seleccionar? ")

    if divisa in divisas:
        print("El simbolo del", divisa, "es", divisas[divisa])
        
    else:
        print("No está dentro del diccionario de divisas.")


def main():
    divisas()

if __name__ == "__main__":
    main()