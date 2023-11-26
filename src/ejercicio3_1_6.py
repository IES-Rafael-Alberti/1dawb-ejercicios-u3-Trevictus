""""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

def asignaturas():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = []
    
    for asignatura in asignaturas:
        nota = input("¿Cuanto has sacado en "+asignatura+"?")
        notas.append(nota)

    asignaturasrepetidas = []

    for i in range(len(asignaturas)):
        if int(notas[i]) < 5:
            asignaturasrepetidas.append(asignaturas[i])

    print("Las asignaturas que vas a repetir son:")
    for asignatura in asignaturasrepetidas:
        
        print(asignatura)


def main():
    asignaturas()

if __name__ == "__main__":
    main()