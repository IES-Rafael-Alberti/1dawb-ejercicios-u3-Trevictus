"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste"""


def datos_personales():

    cestacompra = {}
    camion = True

    while camion:
        clave = input('Introduce el articulo a comprar: ')
        valor = input('Intorduce el valor del articulo: ')
        cestacompra[clave] = valor

        if input('¿Quieres agregar más artículos? (s/n): ').lower() == 'n':
            camion = False
            
            print(cestacompra)



def main():
    datos_personales()

if __name__ == "__main__":
    main()