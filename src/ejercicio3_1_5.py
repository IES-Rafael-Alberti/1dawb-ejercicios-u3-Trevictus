"""Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""


def pedir_numeros():
    lista = ["1","2","3","4","5","6","7","8","9","10"]

    lista.reverse()
    listaencadenada = ", ".join(lista)
    print(listaencadenada, end=".")

    


def main():
    pedir_numeros()

if __name__ == "__main__":
    main()