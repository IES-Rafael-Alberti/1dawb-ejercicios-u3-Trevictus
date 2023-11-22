"""Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios."""

def lista_precios():
    listaprecios= [50, 75, 46, 22, 80, 65, 8]

    print(min(listaprecios))
    print(max(listaprecios))


def main():
    lista_precios()


if __name__ == "__main__":
    main()