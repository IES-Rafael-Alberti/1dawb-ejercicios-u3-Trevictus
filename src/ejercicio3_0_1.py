"""Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente."""

def bucle():
    cadena = len("cadena") -1
    cont = 0
    while cont < cadena:
        if cont == 0:
            cadena.pop(cont)
            cadena
        cont =- 1
    print(cadena)




bucle()