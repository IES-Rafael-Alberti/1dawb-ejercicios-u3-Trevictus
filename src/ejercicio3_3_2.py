"""Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria."""


def solicitar_primaria():
    escuelaprimaria = set()
    escuelasecundaria = set()
    camion = True
    while camion:
        primaria = input("Introduce los alumnos de primaria (x/para salir): ")
        escuelaprimaria.add(primaria.title())
        if primaria == "X".lower():
            camion = False

    oruga = True
    while oruga:
        secundaria = input("Introduce los nombres de los alumnos de secundaria (x/para salir): ")
        escuelasecundaria.add(secundaria.title())
        if secundaria == "X".lower():
            oruga = False

    escuelaprimaria.remove("X")
    escuelasecundaria.remove("X")
    

    print(escuelaprimaria | escuelasecundaria)

    print(escuelaprimaria & escuelasecundaria)

    print(escuelaprimaria - escuelasecundaria)

    print(escuelaprimaria <= escuelasecundaria)




def main():
    solicitar_primaria()



if __name__ == "__main__":
    main()