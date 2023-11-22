"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""

def datos_personales():
    listin = {}

    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    direccion = input("Introduce tu dirección: ")
    telefono = input("Introduce tu telefono: ")

    listin["nombre"] = nombre
    listin["edad"] = edad
    listin["dirección"] = direccion
    listin["teléfono"] = telefono

    print(listin["nombre"],"tiene", listin["edad"],"años, vive en", listin["dirección"],"y su nº de teléfono es", listin["teléfono"])



def main():
    datos_personales()

if __name__ == "__main__":
    main()