"""Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

def datos_personales():

    informacion = {}
    camion = True

    while camion:
        clave = input('Introduce la clave del dato: ')
        valor = input('Intorduce el valor de la clave anterior: ')
        informacion[clave] = valor
        print(informacion)

        if input('¿Quieres agregar más datos? (s/n): ').lower() == 'n':
            camion = False

def main():            
    datos_personales()


if __name__ == "__main__":
    main()